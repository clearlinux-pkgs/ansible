#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible
Version  : 2.0.2.0
Release  : 19
URL      : http://releases.ansible.com/ansible/ansible-2.0.2.0.tar.gz
Source0  : http://releases.ansible.com/ansible/ansible-2.0.2.0.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: ansible-bin
Requires: ansible-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: 0001-Fix-tabs.patch
Patch2: 0001-Look-for-roles-in-usr.patch
Patch3: 0001-no-sftp.patch
Patch4: 0001-no-tt.patch

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

%description python
python components for the ansible package.


%prep
%setup -q -n ansible-2.0.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-vault

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
