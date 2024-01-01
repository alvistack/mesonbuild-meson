# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-meson
Epoch: 100
Version: 1.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: High-productivity build system
License: Apache-2.0
URL: https://github.com/mesonbuild/meson/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Meson is a build system designed to increase programmer productivity. It
does this by providing a fast, simple and easy to use interface for
modern software development tools and practices.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/meson|" data/macros.meson
mkdir -p %{buildroot}%{_prefix}/lib/rpm/macros.d
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/rpm/macros.d data/macros.meson
mkdir -p %{buildroot}%{_prefix}/share/bash-completion/completions
install -Dpm644 -t %{buildroot}%{_prefix}/share/bash-completion/completions data/shell-completions/bash/meson
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n meson
Summary: High-productivity build system
Requires: ninja >= 1.8.2
Requires: python3
Requires: python3-setuptools
Provides: python3-meson = %{epoch}:%{version}-%{release}
Provides: python3dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson) = %{epoch}:%{version}-%{release}

%description -n meson
Meson is a build system designed to increase programmer productivity. It
does this by providing a fast, simple and easy to use interface for
modern software development tools and practices.

%files -n meson
%license COPYING
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_bindir}/meson
%{_datadir}/bash-completion/completions/meson
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_mandir}/man1/*
%{_prefix}/lib/rpm/macros.d/macros.meson
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n meson
Summary: High-productivity build system
Requires: ninja >= 1.8.2
Requires: python3
Requires: python3-setuptools
Provides: python3-meson = %{epoch}:%{version}-%{release}
Provides: python3dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson) = %{epoch}:%{version}-%{release}

%description -n meson
Meson is a build system designed to increase programmer productivity. It
does this by providing a fast, simple and easy to use interface for
modern software development tools and practices.

%files -n meson
%license COPYING
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_bindir}/meson
%{_datadir}/bash-completion/completions/meson
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_mandir}/man1/*
%{_prefix}/lib/rpm/macros.d/macros.meson
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n meson
Summary: High-productivity build system
Requires: ninja-build >= 1.8.2
Requires: python3
Requires: python3-setuptools
Provides: python3-meson = %{epoch}:%{version}-%{release}
Provides: python3dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(meson) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-meson = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(meson) = %{epoch}:%{version}-%{release}

%description -n meson
Meson is a build system designed to increase programmer productivity. It
does this by providing a fast, simple and easy to use interface for
modern software development tools and practices.

%files -n meson
%license COPYING
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_bindir}/meson
%{_datadir}/bash-completion/completions/meson
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_mandir}/man1/*
%{_prefix}/lib/rpm/macros.d/macros.meson
%{python3_sitelib}/*
%endif

%changelog
