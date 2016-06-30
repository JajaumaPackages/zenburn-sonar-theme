Name:           zenburn-sonar-theme
Version:        0.6
Release:        1%{?dist}
Summary:        Branded fork of original Zenburn theme from AwesomeWM

License:        GPLv2
URL:            https://github.com/Jajauma/zenburn-sonar-theme
# git clone https://github.com/Jajauma/zenburn-sonar-theme
# cd zenburn-sonar-theme
# mkdir build && cd build
# cmake .. && make package_source
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  cmake >= 3.0.0
BuildRequires:  ImageMagick
Requires:       awesome

%description
This package provides customized theme based on the original zenburn AwesomeWM
theme.


%prep
%setup -q


%build
mkdir build
pushd build
%cmake -DAWESOME_THEMES_PATH=%{_datadir}/awesome/themes ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%files
%doc LICENSE
%{_datadir}/awesome/themes/zenburn-sonar/


%changelog
* Thu Jun 30 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.6-1
- Public release
