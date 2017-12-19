#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible
Version  : 2.3.2.0
Release  : 46
URL      : https://releases.ansible.com/ansible/ansible-2.3.2.0.tar.gz
Source0  : https://releases.ansible.com/ansible/ansible-2.3.2.0.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+
Requires: ansible-bin
Requires: ansible-python3
Requires: ansible-python
Requires: Jinja2
Requires: PyYAML
Requires: boto3
Requires: botocore
Requires: coverage
Requires: nose
Requires: paramiko
Requires: passlib
Requires: pycrypto
Requires: pytest
Requires: python-memcached
Requires: python-mock
Requires: python-systemd
Requires: redis
Requires: setuptools
Requires: unittest2
BuildRequires : go
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-systemd
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Look-for-roles-in-usr.patch
Patch2: 0001-try-scp-first.patch

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and orchestration engine. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%package bin
Summary: bin components for the ansible package.
Group: Binaries

%description bin
bin components for the ansible package.


%package python
Summary: python components for the ansible package.
Group: Default
Requires: ansible-python3

%description python
python components for the ansible package.


%package python3
Summary: python3 components for the ansible package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ansible package.


%prep
%setup -q -n ansible-2.3.2.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507148528
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible
/usr/bin/ansible-connection
/usr/bin/ansible-console
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-vault

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
