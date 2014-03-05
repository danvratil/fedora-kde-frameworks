# There's nothing to debug
%global debug_package   %{nil}
#%global snapshot 20140205
%global frameworksversion 4.97.0

Name:           extra-cmake-modules
Version:        0.0.11
Epoch:          1
Release:        1
Summary:        Additional modules for CMake build system
BuildArch:      noarch

License:        BSD
URL:            http://www.kde.org

# git archive --format=tar --prefix=%{name}-%{version}/ \
#             --remote=git://anongit.kde.org/%{name},git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        http://download.kde.org/unstable/frameworks/%{frameworksversion}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  kf5-filesystem

Requires:       cmake
Requires:       kf5-filesystem

%description
Additional modules for CMake build system needed by KDE Frameworks.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
%make_install -C %{_target_platform}

%files
%doc README.md COPYING-CMAKE-SCRIPTS
%{_kf5_datadir}/ECM



%changelog
* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 1:0.0.11-1
- Update to KDE Frameworks 5 Alpha 2 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.10-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.10-0.1.20140205git
- Update to pre-relase snapshot of 0.0.10

* Thu Jan 16 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.9-2
- don't generate debuginfo
- rebulild against updated kf5-filesystem

* Thu Jan  9 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.9-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Tue Jan  7 2014 Daniel Vrátil <dvratil@redhat.com> 1:0.0.9-0.1.20140104git
- Match version with upstream: 0.0.9 (ECM is not a framework, it does not follow the 5.x.x scheme)

* Mon Jan  6 2014 Daniel Vrátil <dvraitl@redhat.com> 5.0.0-0.2.201409104git
- Include patch to prevent ECMGenerateHeaders from generating "//" in include paths
  (fixes build of solid and kdnssd frameworks)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com> 5.0.0-0.1.201409104git
- Initial version
