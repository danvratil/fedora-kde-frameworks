# There's nothing to debug
%global debug_package   %{nil}
%define framework umbrella
#%define snapshot 20140205

Name:           kf5-%{framework}
Version:        5.2.0
Epoch:          1
Release:        1%{?dist}
Summary:        CMake configuration for KDE Frameworks 5

License:        GPLv2+
URL:            http://www.kde.org

# git archive --format=tar --prefix=kf5umbrella-%{version}/ \
#             --remote=git://anongit.kde.org/kf5umbrella,git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        kf5umbrella-%{version}-%{snapshot}git.tar.bz2
Source0:        http://download.kde.org/stable/frameworks/%{version}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

%description
Provides CMake configuration file for KDE Frameworks 5


%prep
%setup -q -n umbrella-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%doc README.md
%{_kf5_libdir}/cmake/KF5


%changelog
* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Thu Jul 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-1
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 1:4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 1:4.97.0-1
- Update to KDE Frameworks 5 Alpha 2 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 1:4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.10-0.1.20140205git
- Update to pre-release snapshot of 0.0.10

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Thu Jan  9 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version

