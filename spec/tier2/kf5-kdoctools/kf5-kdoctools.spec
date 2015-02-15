%global framework kdoctools

Name:           kf5-%{framework}
Version:        5.7.0
Release:        3%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for generating documentation

License:        GPLv2+ and MIT
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kdoctools-devel

BuildRequires:  kf5-karchive-devel

Requires:       docbook-dtds
Requires:       docbook-style-xsl
Requires:       kf5-filesystem

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kdoctools-static = %{version}-%{release}
Requires:       kf5-karchive-devel
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        User documentation and help for %{name}
Requires:       kf5-filesystem
%description    doc
Documentation and user help for %{name}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kdoctools5_qt --with-qt --with-man --with-kde --all-name


%files -f kdoctools5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/checkXML5
%{_kf5_bindir}/meinproc5
%{_kf5_datadir}/man/man1/*
%{_kf5_datadir}/man/man7/*
%{_kf5_datadir}/man/man8/*
%{_kf5_datadir}/kf5/kdoctools

%files devel
%{_kf5_includedir}/XsltKde
%{_kf5_libdir}/libKF5XsltKde.a
%{_kf5_libdir}/cmake/KF5DocTools

%files doc
%{_kf5_docdir}/HTML/*/kdoctools5-common


%changelog
* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Thu Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Mon Dec 08 2014 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-1
- KDE Frameworks 5.5.0

* Mon Nov 03 2014 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- KDE Frameworks 5.4.0

* Tue Oct 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.3.0

* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Wed Jun 25 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-3
- Add Provides -static to -devel (RHBZ#1113070)
- Add Requires kf5-filesystem to -doc
- Remove %%post and %%postun ldconfig, there are no shared libs

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-2
- Fix license
- Fix installation of man pages

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Sun May 18 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-3
- Apply upstream patch to improve error reporting in meinproc

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-1
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Sat Mar 15 2014 Jan Grulich <jgrulich@redhat.com 4.97.0-2
- pickup upstream patches

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-relase snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Tue Jan  7 2014 Daniel Vrátil <dvratil@redhat.com>
- add docboox-style-xsl to Requires

* Tue Jan  7 2014 Daniel Vrátil <dvratil@redhat.com>
- add docbook-dtds to Requries, needed for meinproc to actually work

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
