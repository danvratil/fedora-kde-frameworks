%global         git_date    20150122
%global         git_commit  f548510


Name:           ktp-approver
Summary:        KDE Channel Approver for Telepathy
Version:        0.9.60
Release:        1.%{git_date}git%{git_commit}%{?dist}

License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/network/telepathy/%{name}
#Source0:       http://download.kde.org/stable/kde-telepathy/%{version}/src/%{name}-%{version}.tar.bz2

# git archive --format=tar.gz --remote=git://anongit.kde.org/%%{name}.git \
#             --prefix=%%{name}-%%{version}/ --output=%%{name}-%%{git_commit}.tar.gz %%{git_commit}
Source0:        %{name}-%{git_commit}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kservice-devel

BuildRequires:  telepathy-qt5-devel

Obsoletes:      telepathy-kde-approver < 0.3.0
Provides:       telepathy-kde-approver = %{version}-%{release}

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc COPYING
%{_kf5_datadir}/kservicetypes5/ktp-approver.desktop
%{_kf5_datadir}/kservices5/kded/ktp_approver.desktop
%{_kf5_qtplugindir}/kded_ktp_approver.so
%{_sysconfdir}/xdg/ktp_approverrc
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Approver.service


%changelog
* Thu Jan 22 2015 Daniel Vrátil <dvratil@redhat.com> - 0.9.60-1.20150122gitf548510
- Update to experimental KF5 version

* Mon Oct 20 2014 Jan Grulich <jgrulich@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Wed Sep 17 2014 Jan Grulich <jgrulich@redhat.com> - 0.8.80-1
- Update to 0.8.80 (beta)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Jan Grulich <jgrulich@redhat.com> 0.8.1-1
- 0.8.1

* Wed Mar 12 2014 Jan  Grulich <jgrulich@redhat.com> 0.8.0-1
- 0.8.0

* Wed Feb 26 2014 Jan Grulich <jgrulich@redhat.com> - 0.7.80-1
- 0.7.80

* Wed Jan 15 2014 Jan Grulich <jgrulich@redhat.com> 0.7.1-1
- 0.7.1

* Tue Oct 29 2013 Jan Grulich <jgrulich@redhat.com> - 0.7.0-1
- 0,7.0

* Tue Sep 24 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.6.80-1
- 0.6.80

* Tue Aug 06 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.6.3-1
- 0.6.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Jan Grulich <jgrulich@redhat.com> 0.6.2-1
- 0.6.2

* Wed Apr 17 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.1-1
- 0.6.1

* Tue Apr 02 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.0-1
- 0.6.0

* Thu Mar 07 2013 Rex Dieter <rdieter@fedoraproject.org> 0.5.80-1
- 0.5.80

* Sun Feb 17 2013 Jan Grulich <jgrulich@redhat.com> - 0.5.3-1
- 0.5.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jan Grulich <jgrulich@redhat.com> - 0.5.2-1
- 0.5.2

* Fri Oct 05 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-1
- 0.5.1

* Thu Jul 26 2012 Jan Grulich <jgrulich@redhat.com> - 0.4.1-1
- 0.4.1

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-3
- disable debug output

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-1
- 0.4.0

* Mon Apr 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-1
- 0.3.1

* Fri Feb 10 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-2
- drop BR: telepathy-qt4-devel

* Tue Jan 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- ktp-approver-0.3.0

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-1
- 0.2.0

* Wed Sep 14 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-2
- License: LGPLv2+
- fix Source0 URL
- fix tabs/spaces

* Fri Aug 12 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-1
- first try

