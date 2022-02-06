%global debug_package %{nil}

Name: python-meson
Epoch: 100
Version: 0.61.2
Release: 1%{?dist}
BuildArch: noarch
Summary: High-productivity build system
License: Apache-2.0
URL: https://github.com/mesonbuild/meson/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
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
%fdupes -s %{buildroot}%{python3_sitelib}

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
