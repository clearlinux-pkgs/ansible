#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible
Version  : 2.7.9
Release  : 79
URL      : https://github.com/ansible/ansible/archive/v2.7.9.tar.gz
Source0  : https://github.com/ansible/ansible/archive/v2.7.9.tar.gz
Summary  : SSH-based application deployment, configuration management, and IT orchestration platform
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+
Requires: ansible-bin = %{version}-%{release}
Requires: ansible-license = %{version}-%{release}
Requires: ansible-python = %{version}-%{release}
Requires: ansible-python3 = %{version}-%{release}
Requires: Jinja2
Requires: PyYAML
Requires: cryptography
Requires: paramiko
Requires: python-systemd
Requires: setuptools
Requires: sshpass
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-systemd
BuildRequires : sshpass
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-try-scp-first.patch

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and orchestration engine. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%package bin
Summary: bin components for the ansible package.
Group: Binaries
Requires: ansible-license = %{version}-%{release}

%description bin
bin components for the ansible package.


%package license
Summary: license components for the ansible package.
Group: Default

%description license
license components for the ansible package.


%package python
Summary: python components for the ansible package.
Group: Default
Requires: ansible-python3 = %{version}-%{release}

%description python
python components for the ansible package.


%package python3
Summary: python3 components for the ansible package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ansible package.


%prep
%setup -q -n ansible-2.7.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554229573
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible
cp COPYING %{buildroot}/usr/share/package-licenses/ansible/COPYING
cp packaging/debian/copyright %{buildroot}/usr/share/package-licenses/ansible/packaging_debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible
/usr/bin/ansible-config
/usr/bin/ansible-connection
/usr/bin/ansible-console
/usr/bin/ansible-doc
/usr/bin/ansible-galaxy
/usr/bin/ansible-inventory
/usr/bin/ansible-playbook
/usr/bin/ansible-pull
/usr/bin/ansible-vault

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ansible/COPYING
/usr/share/package-licenses/ansible/packaging_debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
