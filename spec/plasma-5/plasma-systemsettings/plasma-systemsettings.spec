%define         base_name systemsettings

Name:           plasma-%{base_name}
Version:        5.2.2
Release:        1%{?dist}
Summary:        KDE's System Settings application

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/systemsettings

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel

BuildRequires:  desktop-file-utils

Requires:       kf5-filesystem

# kde-cli-tools provides kcmshell5, which is not directly needed by
# systemsettings, but is an addition expected by users
Requires:       kde-cli-tools

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{base_name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang systemsettings5 --with-qt --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kdesystemsettings.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/systemsettings.desktop


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f systemsettings5.lang
%doc COPYING COPYING.DOC
%{_bindir}/systemsettings5
%{_libdir}/libsystemsettingsview.so.*
%{_kf5_qtplugindir}/*.so
%{_datadir}/systemsettings
%{_datadir}/applications/kdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kxmlgui5/systemsettings
%{_docdir}/HTML/*/systemsettings

%files devel
%{_includedir}/systemsettingsview
%{_libdir}/libsystemsettingsview.so

%changelog
* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Tue Jan 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-2
- Requires: kde-cli-tools (for kcmshell5)

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Tue Jan 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

* Mon Jan 05 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.1-2
- Better URL
  Used make install instead of make_install macro
  Added desktop file validation
  Fixed search for localization

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Thu Jul 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Thu May 15 2014 Daniel Vrátil <dvratil@redhat.com> - 4.90.1-1.20140515git0cab60e
- Intial snapshot