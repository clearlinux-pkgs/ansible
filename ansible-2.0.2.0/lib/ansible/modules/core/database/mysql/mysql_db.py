#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Mark Theunissen <mark.theunissen@gmail.com>
# Sponsored by Four Kitchens http://fourkitchens.com.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: mysql_db
short_description: Add or remove MySQL databases from a remote host.
description:
   - Add or remove MySQL databases from a remote host.
version_added: "0.6"
options:
  name:
    description:
      - name of the database to add or remove
      - name=all May only be provided if I(state) is C(dump) or C(import).
      - if name=all Works like --all-databases option for mysqldump (Added in 2.0)
    required: true
    default: null
    aliases: [ db ]
  state:
    description:
      - The database state
    required: false
    default: present
    choices: [ "present", "absent", "dump", "import" ]
  collation:
    description:
      - Collation mode (sorting). This only applies to new table/databases and does not update existing ones, this is a limitation of MySQL.
    required: false
    default: null
  encoding:
    description:
      - Encoding mode
    required: false
    default: null
  target:
    description:
      - Location, on the remote host, of the dump file to read from or write to. Uncompressed SQL
        files (C(.sql)) as well as bzip2 (C(.bz2)), gzip (C(.gz)) and xz (Added in 2.0) compressed files are supported.
    required: false
author: "Ansible Core Team"
extends_documentation_fragment: mysql
'''

EXAMPLES = '''
# Create a new database with name 'bobdata'
- mysql_db: name=bobdata state=present

# Copy database dump file to remote host and restore it to database 'my_db'
- copy: src=dump.sql.bz2 dest=/tmp
- mysql_db: name=my_db state=import target=/tmp/dump.sql.bz2

# Dumps all databases to hostname.sql
- mysql_db: state=dump name=all target=/tmp/{{ inventory_hostname }}.sql

# Imports file.sql similiar to mysql -u <username> -p <password> < hostname.sql
- mysql_db: state=import name=all target=/tmp/{{ inventory_hostname }}.sql
'''

import os
import pipes
import stat
import subprocess

try:
    import MySQLdb
except ImportError:
    mysqldb_found = False
else:
    mysqldb_found = True

# ===========================================
# MySQL module specific support methods.
#

def db_exists(cursor, db):
    res = cursor.execute("SHOW DATABASES LIKE %s", (db.replace("_","\_"),))
    return bool(res)

def db_delete(cursor, db):
    query = "DROP DATABASE %s" % mysql_quote_identifier(db, 'database')
    cursor.execute(query)
    return True

def db_dump(module, host, user, password, db_name, target, all_databases, port, config_file, socket=None, ssl_cert=None, ssl_key=None, ssl_ca=None):
    cmd = module.get_bin_path('mysqldump', True)
    # If defined, mysqldump demands --defaults-extra-file be the first option
    if config_file:
        cmd += " --defaults-extra-file=%s" % pipes.quote(config_file)
    cmd += " --quick"
    if user is not None:
        cmd += " --user=%s" % pipes.quote(user)
    if password is not None:
        cmd += " --password=%s" % pipes.quote(password)
    if ssl_cert is not None:
        cmd += " --ssl-cert=%s" % pipes.quote(ssl_cert)
    if ssl_key is not None:
        cmd += " --ssl-key=%s" % pipes.quote(ssl_key)
    if ssl_cert is not None:
        cmd += " --ssl-ca=%s" % pipes.quote(ssl_ca)
    if socket is not None:
        cmd += " --socket=%s" % pipes.quote(socket)
    else:
        cmd += " --host=%s --port=%i" % (pipes.quote(host), port)
    if all_databases:
        cmd += " --all-databases"
    else:
        cmd += " %s" % pipes.quote(db_name)

    path = None
    if os.path.splitext(target)[-1] == '.gz':
        path = module.get_bin_path('gzip', True)
    elif os.path.splitext(target)[-1] == '.bz2':
        path = module.get_bin_path('bzip2', True)
    elif os.path.splitext(target)[-1] == '.xz':
        path = module.get_bin_path('xz', True)

    if path:
        cmd = '%s | %s > %s' % (cmd, path, pipes.quote(target))
    else:
        cmd += " > %s" % pipes.quote(target)

    rc, stdout, stderr = module.run_command(cmd, use_unsafe_shell=True)
    return rc, stdout, stderr

def db_import(module, host, user, password, db_name, target, all_databases, port, config_file, socket=None, ssl_cert=None, ssl_key=None, ssl_ca=None):
    if not os.path.exists(target):
        return module.fail_json(msg="target %s does not exist on the host" % target)

    cmd = [module.get_bin_path('mysql', True)]
    # --defaults-file must go first, or errors out
    if config_file:
        cmd.append("--defaults-extra-file=%s" % pipes.quote(config_file))
    if user:
        cmd.append("--user=%s" % pipes.quote(user))
    if password:
        cmd.append("--password=%s" % pipes.quote(password))
    if socket is not None:
        cmd.append("--socket=%s" % pipes.quote(socket))
    if ssl_cert is not None:
        cmd.append("--ssl-cert=%s" % pipes.quote(ssl_cert))
    if ssl_key is not None:
        cmd.append("--ssl-key=%s" % pipes.quote(ssl_key))
    if ssl_cert is not None:
        cmd.append("--ssl-ca=%s" % pipes.quote(ssl_ca))
    else:
        cmd.append("--host=%s" % pipes.quote(host))
        cmd.append("--port=%i" % port)
    if not all_databases:
        cmd.append("-D")
        cmd.append(pipes.quote(db_name))

    comp_prog_path = None
    if os.path.splitext(target)[-1] == '.gz':
        comp_prog_path = module.get_bin_path('gzip', required=True)
    elif os.path.splitext(target)[-1] == '.bz2':
        comp_prog_path = module.get_bin_path('bzip2', required=True)
    elif os.path.splitext(target)[-1] == '.xz':
        comp_prog_path = module.get_bin_path('xz', required=True)

    if comp_prog_path:
        p1 = subprocess.Popen([comp_prog_path, '-dc', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p2 = subprocess.Popen(cmd, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout2, stderr2) = p2.communicate()
        p1.stdout.close()
        p1.wait()
        if p1.returncode != 0:
            stderr1 = p1.stderr.read()
            return p1.returncode, '', stderr1
        else:
            return p2.returncode, stdout2, stderr2
    else:
        cmd = ' '.join(cmd)
        cmd += " < %s" % pipes.quote(target)
        rc, stdout, stderr = module.run_command(cmd, use_unsafe_shell=True)
        return rc, stdout, stderr

def db_create(cursor, db, encoding, collation):
    query_params = dict(enc=encoding, collate=collation)
    query = ['CREATE DATABASE %s' % mysql_quote_identifier(db, 'database')]
    if encoding:
        query.append("CHARACTER SET %(enc)s")
    if collation:
        query.append("COLLATE %(collate)s")
    query = ' '.join(query)
    res = cursor.execute(query, query_params)
    return True

# ===========================================
# Module execution.
#

def main():
    module = AnsibleModule(
        argument_spec = dict(
            login_user=dict(default=None),
            login_password=dict(default=None),
            login_host=dict(default="localhost"),
            login_port=dict(default=3306, type='int'),
            login_unix_socket=dict(default=None),
            name=dict(required=True, aliases=['db']),
            encoding=dict(default=""),
            collation=dict(default=""),
            target=dict(default=None),
            state=dict(default="present", choices=["absent", "present","dump", "import"]),
            ssl_cert=dict(default=None),
            ssl_key=dict(default=None),
            ssl_ca=dict(default=None),
            config_file=dict(default="~/.my.cnf"),
        )
    )

    if not mysqldb_found:
        module.fail_json(msg="the python mysqldb module is required")

    db = module.params["name"]
    encoding = module.params["encoding"]
    collation = module.params["collation"]
    state = module.params["state"]
    target = module.params["target"]
    socket = module.params["login_unix_socket"]
    login_port = module.params["login_port"]
    if login_port < 0 or login_port > 65535:
        module.fail_json(msg="login_port must be a valid unix port number (0-65535)")
    ssl_cert = module.params["ssl_cert"]
    ssl_key = module.params["ssl_key"]
    ssl_ca = module.params["ssl_ca"]
    config_file = module.params['config_file']
    config_file = os.path.expanduser(os.path.expandvars(config_file))
    login_password = module.params["login_password"]
    login_user = module.params["login_user"]
    login_host = module.params["login_host"]

    # make sure the target path is expanded for ~ and $HOME
    if target is not None:
        target = os.path.expandvars(os.path.expanduser(target))

    if state in ['dump','import']:
        if target is None:
            module.fail_json(msg="with state=%s target is required" % (state))
        if db == 'all':
            db = 'mysql'
            all_databases = True
        else:
            all_databases = False
    else:
        if db == 'all':
            module.fail_json(msg="name is not allowed to equal 'all' unless state equals import, or dump.")
    try:
        cursor = mysql_connect(module, login_user, login_password, config_file, ssl_cert, ssl_key, ssl_ca)
    except Exception, e:
        if os.path.exists(config_file):
            module.fail_json(msg="unable to connect to database, check login_user and login_password are correct or %s has the credentials. Exception message: %s" % (config_file, e))
        else:
            module.fail_json(msg="unable to find %s. Exception message: %s" % (config_file, e))

    changed = False
    if not os.path.exists(config_file):
        config_file = None
    if db_exists(cursor, db):
        if state == "absent":
            try:
                changed = db_delete(cursor, db)
            except Exception, e:
                module.fail_json(msg="error deleting database: " + str(e))
        elif state == "dump":
            rc, stdout, stderr = db_dump(module, login_host, login_user,
                                        login_password, db, target, all_databases,
                                        login_port, config_file, socket, ssl_cert, ssl_key, ssl_ca)
            if rc != 0:
                module.fail_json(msg="%s" % stderr)
            else:
                module.exit_json(changed=True, db=db, msg=stdout)
        elif state == "import":
            rc, stdout, stderr = db_import(module, login_host, login_user,
                                        login_password, db, target, all_databases,
                                        login_port, config_file, socket, ssl_cert, ssl_key, ssl_ca)
            if rc != 0:
                module.fail_json(msg="%s" % stderr)
            else:
                module.exit_json(changed=True, db=db, msg=stdout)
    else:
        if state == "present":
            try:
                changed = db_create(cursor, db, encoding, collation)
            except Exception, e:
                module.fail_json(msg="error creating database: " + str(e))

    module.exit_json(changed=changed, db=db)

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.database import *
from ansible.module_utils.mysql import *
if __name__ == '__main__':
    main()
