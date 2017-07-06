#
# (c) 2015, Peter Sprygada <psprygada@ansible.com>
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


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = """
options:
  host:
    description:
      - Specifies the DNS host name or address for connecting to the remote
        device over the specified transport.  The value of host is used as
        the destination address for the transport.
    required: true
  port:
    description:
      - Specifies the port to use when buiding the connection to the remote
        device.  This value applies to either I(cli) or I(nxapi).  The port
        value will default to the approriate transport common port if
        none is provided in the task.  (cli=22, http=80, https=443).
    required: false
    default: 0 (use common port)
  username:
    description:
      - Configures the usename to use to authenticate the connection to
        the remote device.  The value of I(username) is used to authenticate
        either the CLI login or the nxapi authentication depending on which
        transport is used.
    required: true
  password:
    description:
      - Specifies the password to use when authentication the connection to
        the remote device.  This is a common argument used for either I(cli)
        or I(nxapi) transports.
    required: false
    default: null
  transport:
    description:
      - Configures the transport connection to use when connecting to the
        remote device.  The transport argument supports connectivity to the
        device over cli (ssh) or nxapi.
    required: true
    default: cli
  use_ssl:
    description:
      - Configures the I(transport) to use SSL if set to true only when the
        I(transport) argument is configured as nxapi.  If the transport
        argument is not nxapi, this value is ignored
    required: false
    default: false
    choices: BOOLEANS

"""
