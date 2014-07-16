%define framework kunitconversion

Name:           kf5-%{framework}
Version:        5.0.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for unit conversions

License:        LGPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        http://download.kde.org/stable/frameworks/%{version}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kconfig-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 2 addon for unit conversions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel
Requires:       kf5-kconfig-devel


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
%find_lang kunitconversion5_qt --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f kunitconversion5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5UnitConversion.so.*

%files devel
%{_kf5_includedir}/kunitconversion_version.h
%{_kf5_includedir}/KUnitConversion
%{_kf5_libdir}/libKF5UnitConversion.so
%{_kf5_libdir}/cmake/KF5UnitConversion
%{_kf5_archdatadir}/mkspecs/modules/qt_KUnitConversion.pri


%changelog
* Thu Jul 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Thu Jun 12 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-2
- Upgrade to Tier2 framework

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

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version