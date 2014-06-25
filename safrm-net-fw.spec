%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:       safrm-net-fw
Summary:    Collection of utilities from safrm.net 
Version:    1.0.0
Release:    1
Group:      Development/Tools
License:    LGPL v2.1
BuildArch:  noarch
URL:        http://safrm.net/
Vendor:     Miroslav Safr <miroslav.safr@gmail.com>
Source0:    %{name}-%{version}.tar.bz2
Autoreq:    on
Autoreqprov: on
BuildRequires: appver >= 1.1.1
BuildRequires: jenkins-support-scripts >= 1.2.3
Requires: af
Requires: appver
Requires: easybrain 
Requires: efind 
Requires: gr-scripts
Requires: jenkins-support-scripts 
Requires: pkgcheck 
Requires: rpmmake
Requires: rvmb
Requires: semaphored
Requires: xmlenv

%description
Collection of useful utilities in metapackage \
	from safrm.net

%prep
%setup -c -n ./%{name}-%{version}

%build


%install

%clean
rm -fr %{buildroot}

%check

%files

