#%define snapshot 20140205
%define framework kservice

Name:           kf5-%{framework}
Version:        5.2.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for advanced plugin and service introspection

License:        GPLv2+ and LGPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        http://download.kde.org/stable/frameworks/%{version}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kdoctools-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 solution for advanced plugin and service
introspection.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kcrash-devel
Requires:       kf5-kdbusaddons-devel
Requires:       kf5-ki18n-devel
Requires:       kf5-kdoctools-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang kservice5_qt --with-qt --all-name

mv %{buildroot}/%{_kf5_sysconfdir}/xdg/menus/applications.menu %{buildroot}/%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f kservice5_qt.lang
%doc COPYING COPYING.LIB README.md
%config %{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu
%{_kf5_bindir}/kbuildsycoca5
%{_kf5_libdir}/libKF5Service.so.*
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man8/*

%files devel
%{_kf5_includedir}/kservice_version.h
%{_kf5_includedir}/KService
%{_kf5_bindir}/desktoptojson
%{_kf5_libdir}/libKF5Service.so
%{_kf5_libdir}/cmake/KF5Service
%{_kf5_archdatadir}/mkspecs/modules/qt_KService.pri


%changelog
* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-relase snapshot of 4.96.0

* Thu Jan 16 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-2
- rebuild against new kf5-filesystem

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
