#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD05E6034F8B58C16 (ansible-gha@redhat.com)
#
Name     : ansible
Version  : 4.8.0
Release  : 143
URL      : https://files.pythonhosted.org/packages/ac/17/cb3ae6e4ae5b2d936ec5bf7e20cb91814e3af3ed27bbfcdf8a7253a016d5/ansible-4.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/17/cb3ae6e4ae5b2d936ec5bf7e20cb91814e3af3ed27bbfcdf8a7253a016d5/ansible-4.8.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/ac/17/cb3ae6e4ae5b2d936ec5bf7e20cb91814e3af3ed27bbfcdf8a7253a016d5/ansible-4.8.0.tar.gz.asc
Summary  : Radically simple IT automation
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 GPL-3.0+ MIT
Requires: ansible-python = %{version}-%{release}
Requires: ansible-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ansible_compat)
BuildRequires : pypi(ansible_core)
BuildRequires : pypi(appdirs)
BuildRequires : pypi(arrow)
BuildRequires : pypi(asn1crypto)
BuildRequires : pypi(astroid)
BuildRequires : pypi(atomicwrites)
BuildRequires : pypi(attrs)
BuildRequires : pypi(awxkit)
BuildRequires : pypi(azure_common)
BuildRequires : pypi(azure_mgmt_compute)
BuildRequires : pypi(azure_mgmt_core)
BuildRequires : pypi(azure_mgmt_netapp)
BuildRequires : pypi(azure_mgmt_network)
BuildRequires : pypi(azure_mgmt_resource)
BuildRequires : pypi(azure_mgmt_storage)
BuildRequires : pypi(black)
BuildRequires : pypi(boto)
BuildRequires : pypi(boto3)
BuildRequires : pypi(botocore)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(chardet)
BuildRequires : pypi(click)
BuildRequires : pypi(colorama)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(cs)
BuildRequires : pypi(docker)
BuildRequires : pypi(google_auth)
BuildRequires : pypi(idna)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(infi.dtypes.iqn)
BuildRequires : pypi(infi.dtypes.wwn)
BuildRequires : pypi(inspursmsdk)
BuildRequires : pypi(ipaddr)
BuildRequires : pypi(ipaddress)
BuildRequires : pypi(isort)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jmespath)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(jxmlease)
BuildRequires : pypi(lazy_object_proxy)
BuildRequires : pypi(lxml)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(mccabe)
BuildRequires : pypi(molecule)
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(msrestazure)
BuildRequires : pypi(munch)
BuildRequires : pypi(ncclient)
BuildRequires : pypi(netaddr)
BuildRequires : pypi(netapp_lib)
BuildRequires : pypi(openshift)
BuildRequires : pypi(ordereddict)
BuildRequires : pypi(packaging)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(pbr)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(poetry_core)
BuildRequires : pypi(purestorage)
BuildRequires : pypi(purity_fb)
BuildRequires : pypi(py)
BuildRequires : pypi(pycodestyle)
BuildRequires : pypi(pycountry)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pylint)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pysnow)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(regex)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_oauthlib)
BuildRequires : pypi(requests_toolbelt)
BuildRequires : pypi(ruamel.yaml)
BuildRequires : pypi(ruamel.yaml.clib)
BuildRequires : pypi(scp)
BuildRequires : pypi(selectors2)
BuildRequires : pypi(sentinels)
BuildRequires : pypi(simplejson)
BuildRequires : pypi(six)
BuildRequires : pypi(textfsm)
BuildRequires : pypi(toml)
BuildRequires : pypi(ttp)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(urlobject)
BuildRequires : pypi(voluptuous)
BuildRequires : pypi(wcwidth)
BuildRequires : pypi(wheel)
BuildRequires : pypi(wrapt)
BuildRequires : pypi(xmljson)
BuildRequires : pypi(xmltodict)
BuildRequires : pypi(zabbix_api)
BuildRequires : pypi(zipp)

%description
*******
        Ansible
        *******
        
        Ansible is a radically simple IT automation system. It handles configuration management, application
        deployment, cloud provisioning, ad-hoc task execution, network automation, and multi-node
        orchestration. Ansible makes complex changes like zero-downtime rolling updates with load balancers

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
Requires: ansible-core
Requires: pypi(ansible_core)

%description python3
python3 components for the ansible package.


%prep
%setup -q -n ansible-4.8.0
cd %{_builddir}/ansible-4.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641935431
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . ansible-core
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ansible
cp %{_builddir}/ansible-4.8.0/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/amazon/aws/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/ansible/netcommon/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/ansible/posix/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/ansible/utils/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/ansible/windows/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/arista/eos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/awx/awx/COPYING %{buildroot}/usr/share/package-licenses/ansible/8eb83a42d183d11f2ab1e7e2041b9762e8d935c6
cp %{_builddir}/ansible-4.8.0/ansible_collections/azure/azcollection/LICENSE %{buildroot}/usr/share/package-licenses/ansible/7bc5474bacf20ef085e04ded37c5e604c197cf07
cp %{_builddir}/ansible-4.8.0/ansible_collections/chocolatey/chocolatey/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/aci/LICENSE %{buildroot}/usr/share/package-licenses/ansible/2e71dbd548f00d2365bdfc32072909fbc5703db6
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/asa/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/intersight/LICENSE.txt %{buildroot}/usr/share/package-licenses/ansible/7fd6360e370eb278e4f6298b830a6d4024667aa7
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/ios/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/iosxr/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/mso/LICENSE %{buildroot}/usr/share/package-licenses/ansible/2e71dbd548f00d2365bdfc32072909fbc5703db6
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/nso/LICENSE %{buildroot}/usr/share/package-licenses/ansible/37cfd8ca335069ea657b6cfd2eac89cdd2954561
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/nxos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cisco/ucs/LICENSE.txt %{buildroot}/usr/share/package-licenses/ansible/b21b197221daa7edc4bbf5880b2f774912d2455d
cp %{_builddir}/ansible-4.8.0/ansible_collections/cloudscale_ch/cloud/COPYING %{buildroot}/usr/share/package-licenses/ansible/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/aws/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/azure/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/crypto/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/digitalocean/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/docker/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/fortios/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/general/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/google/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/grafana/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/hashi_vault/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/hrobot/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/ansible/7bc5474bacf20ef085e04ded37c5e604c197cf07
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/kubevirt/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/libvirt/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/libvirt/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/mongodb/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/mysql/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/network/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/okd/LICENSE %{buildroot}/usr/share/package-licenses/ansible/7bc5474bacf20ef085e04ded37c5e604c197cf07
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/postgresql/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/proxysql/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/rabbitmq/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/routeros/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/skydive/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/sops/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/vmware/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/vmware/LICENSE %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/windows/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/community/zabbix/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/containers/podman/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/cyberark/conjur/LICENSE %{buildroot}/usr/share/package-licenses/ansible/cc883360726c29a4550e1d0630318e86e5778235
cp %{_builddir}/ansible-4.8.0/ansible_collections/cyberark/pas/LICENSE %{buildroot}/usr/share/package-licenses/ansible/f940ee84768beeb07c1094f57531ded0f1f28d23
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/enterprise_sonic/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/openmanage/COPYING.md %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_aaa/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_acl/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_bfd/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_bgp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_copy_config/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_dns/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_ecmp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_fabric_summary/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_flow_monitor/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_image_upgrade/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_interface/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_lag/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_lldp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_logging/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_network_validation/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_ntp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_prefix_list/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_qos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_raguard/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_route_map/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_snmp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_system/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_template/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_uplink/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_users/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_vlan/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_vlt/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_vrf/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_vrrp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_vxlan/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os10/roles/os10_xstp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_aaa/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_acl/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_bgp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_interface/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_lag/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_lldp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_logging/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_ntp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_qos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_snmp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_system/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_users/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_vlan/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_vrrp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os6/roles/os6_xstp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_aaa/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_acl/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_bgp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_copy_config/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_dcb/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_dns/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_ecmp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_interface/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_lag/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_lldp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_logging/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_ntp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_prefix_list/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_sflow/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_snmp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_system/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_users/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_vlan/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_vlt/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_vrf/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_vrrp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/dellemc/os9/roles/os9_xstp/LICENSE %{buildroot}/usr/share/package-licenses/ansible/1e4dfa9285a1c1939618c127bff0b28a20415fcb
cp %{_builddir}/ansible-4.8.0/ansible_collections/f5networks/f5_modules/plugins/lookup/license_hopper.py %{buildroot}/usr/share/package-licenses/ansible/22cf4767fdced6cc00395c3c56eefff73127d58c
cp %{_builddir}/ansible-4.8.0/ansible_collections/frr/frr/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/gluster/gluster/LICENSE %{buildroot}/usr/share/package-licenses/ansible/e4851650c592eb694000404a0e066e41df28be1f
cp %{_builddir}/ansible-4.8.0/ansible_collections/google/cloud/LICENSE %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/google/cloud/roles/gcloud/LICENSE %{buildroot}/usr/share/package-licenses/ansible/33ab7ec85799c08d1863b02a5aa30c32fb799dca
cp %{_builddir}/ansible-4.8.0/ansible_collections/hetzner/hcloud/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/ibm/qradar/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/infinidat/infinibox/LICENSE %{buildroot}/usr/share/package-licenses/ansible/b04f164721ecb9138e854f0c541806c85c2d5e56
cp %{_builddir}/ansible-4.8.0/ansible_collections/inspur/sm/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/junipernetworks/junos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/kubernetes/core/LICENSE %{buildroot}/usr/share/package-licenses/ansible/7bc5474bacf20ef085e04ded37c5e604c197cf07
cp %{_builddir}/ansible-4.8.0/ansible_collections/mellanox/onyx/LICENSE %{buildroot}/usr/share/package-licenses/ansible/7bc5474bacf20ef085e04ded37c5e604c197cf07
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/aws/COPYING %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/azure/COPYING %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/cloudmanager/COPYING %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/ontap/COPYING %{buildroot}/usr/share/package-licenses/ansible/1de7bacb4fbbd7b6d391a69abfe174c2509ec303
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/ontap/roles/na_ontap_cluster_config/LICENSE %{buildroot}/usr/share/package-licenses/ansible/a2f9ffbf32eeb6284afa81bc4fb4c27b80d044e9
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/ontap/roles/na_ontap_nas_create/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/ontap/roles/na_ontap_san_create/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/ontap/roles/na_ontap_vserver_create/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp/um_info/COPYING %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/netapp_eseries/santricity/COPYING %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/netbox/netbox/LICENSE %{buildroot}/usr/share/package-licenses/ansible/b4d7662bb6b0b804c8fc94f7bc81f59dce0c36f3
cp %{_builddir}/ansible-4.8.0/ansible_collections/ngine_io/cloudstack/COPYING %{buildroot}/usr/share/package-licenses/ansible/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
cp %{_builddir}/ansible-4.8.0/ansible_collections/ngine_io/vultr/COPYING %{buildroot}/usr/share/package-licenses/ansible/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
cp %{_builddir}/ansible-4.8.0/ansible_collections/openstack/cloud/COPYING %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/openvswitch/openvswitch/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/ovirt/ovirt/licenses/Apache-license.txt %{buildroot}/usr/share/package-licenses/ansible/81538fac4f7316ad68eb3218e4c73a7172aac598
cp %{_builddir}/ansible-4.8.0/ansible_collections/ovirt/ovirt/licenses/GPL-license.txt %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/sensu/sensu_go/COPYING %{buildroot}/usr/share/package-licenses/ansible/338650eb7a42dd9bc1f1c6961420f2633b24932d
cp %{_builddir}/ansible-4.8.0/ansible_collections/splunk/es/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/t_systems_mms/icinga_director/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/ansible_collections/theforeman/foreman/LICENSE %{buildroot}/usr/share/package-licenses/ansible/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/ansible-4.8.0/ansible_collections/vyos/vyos/LICENSE %{buildroot}/usr/share/package-licenses/ansible/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/ansible-4.8.0/debian/copyright %{buildroot}/usr/share/package-licenses/ansible/df7eb10107eae3c1fc58f5cfe07af25d35959132
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} ansible-core
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
