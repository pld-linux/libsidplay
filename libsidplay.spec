Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl.UTF-8):	Biblioteka odtwarzająca muzyczki z Commodore 64 i emulująca układ SID
Name:		libsidplay
Version:	1.36.60
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://home.arcor.de/ms2002sep/bak/%{name}-%{version}.tar.bz2
# Source0-md5:	46c5ceccd31636e3f83774dd0b3d4003
# dead together with geocities
#URL:		http://www.geocities.com/SiliconValley/Lakes/5147/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it you
can play musics from Commodore 64 (or compatible) programs.

%description -l pl.UTF-8
Ta biblioteka zawiera emulator układu SID (Sound Interface Device),
który jest używany przez programy odtwarzające muzykę jak np. SIDPLAY.
Przy jej pomocy można odtwarzać muzyczki z programów dla Commodore 64
(i kompatybilnych).

%package devel
Summary:	Header files for compiling apps that use libsidplay
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania aplikacji używających libsidplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files for compiling applications that
use libsidplay.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania aplikacji używających
biblioteki libsidplay.

%package static
Summary:	Static libsidplay library
Summary(pl.UTF-8):	Statyczna biblioteka libsidplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplay.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję libsidplay.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libsidplay.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsidplay.so.1

%files devel
%defattr(644,root,root,755)
%doc DEVELOPER src/fastforward.txt src/mixing.txt src/mpu.txt src/panning.txt
%attr(755,root,root) %{_libdir}/libsidplay.so
%{_libdir}/libsidplay.la
%{_includedir}/sidplay

%files static
%defattr(644,root,root,755)
%{_libdir}/libsidplay.a
