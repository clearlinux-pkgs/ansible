#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ansible
Version  : 2.9.18
Release  : 115
URL      : https://github.com/ansible/ansible/archive/v2.9.18/ansible-2.9.18.tar.gz
Source0  : https://github.com/ansible/ansible/archive/v2.9.18/ansible-2.9.18.tar.gz
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 GPL-3.0+ MIT Python-2.0
Requires: ansible-bin = %{version}-%{release}
Requires: ansible-license = %{version}-%{release}
Requires: ansible-python = %{version}-%{release}
Requires: ansible-python3 = %{version}-%{release}
Requires: Jinja2
Requires: PyYAML
Requires: cryptography
Requires: paramiko
Requires: python-systemd
Requires: sshpass
BuildRequires : Jinja2
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : paramiko
BuildRequires : python-systemd
BuildRequires : sshpass

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
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
Provides: pypi(ansible)
Requires: pypi(cryptography)
Requires: pypi(jinja2)
Requires: pypi(pyyaml)

%description python3
python3 components for the ansible package.


%prep
%setup -q -n ansible-2.9.18
cd %{_builddir}/ansible-2.9.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613763351
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible
cp %{_builddir}/ansible-2.9.18/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-2.9.18/licenses/Apache-License.txt %{buildroot}/usr/share/package-licenses/ansible/c700a8b9312d24bdc57570f7d6a131cf63d89016
cp %{_builddir}/ansible-2.9.18/licenses/MIT-license.txt %{buildroot}/usr/share/package-licenses/ansible/df180fcf964224ba9180a646ca107bfe65595f23
cp %{_builddir}/ansible-2.9.18/licenses/PSF-license.txt %{buildroot}/usr/share/package-licenses/ansible/7b14725671bae6dc04be2b87de58131f0614dfad
cp %{_builddir}/ansible-2.9.18/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/ansible/b7f3dc6d692392795202ab560c7583e986d8352b
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
/usr/bin/ansible-test
/usr/bin/ansible-vault

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
/usr/share/package-licenses/ansible/7b14725671bae6dc04be2b87de58131f0614dfad
/usr/share/package-licenses/ansible/b7f3dc6d692392795202ab560c7583e986d8352b
/usr/share/package-licenses/ansible/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/ansible/df180fcf964224ba9180a646ca107bfe65595f23

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
