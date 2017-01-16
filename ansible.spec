#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible
Version  : 2.2.1.0
Release  : 29
URL      : http://releases.ansible.com/ansible/ansible-2.2.1.0.tar.gz
Source0  : http://releases.ansible.com/ansible/ansible-2.2.1.0.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: ansible-bin
Requires: ansible-python
BuildRequires : Jinja2
BuildRequires : PyYAML
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycrypto
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: Jinja2

%description python
python components for the ansible package.


%prep
%setup -q -n ansible-2.2.1.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484590162
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484590162
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible
/usr/bin/ansible-console
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-vault

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
