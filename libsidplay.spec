Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl):	Biblioteka odtwarzaj±ca muzyczki z Commodore 64 i emuluj±ca uk³ad SID
Name:		libsidplay
Version:	1.36.57
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tgz
# Source0-md5:	a935ec67d5600b079e22ecac58cc19d5
Patch0:		%{name}-gcc34.patch
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it you
can play musics from Commodore 64 (or compatible) programs.

%description -l pl
Ta biblioteka zawiera emulator uk³adu SID (Sound Interface Device),
który jest u¿ywany przez programy odtwarzaj±ce muzykê jak np. SIDPLAY.
Przy jej pomocy mo¿na odtwarzaæ muzyczki z programów dla Commodore 64
(i kompatybilnych).

%package devel
Summary:	Header files for compiling apps that use libsidplay
Summary(pl):	Pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych libsidplay
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for compiling applications that
use libsidplay.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych
biblioteki libsidplay.

%package static
Summary:	Static libsidplay library
Summary(pl):	Statyczna biblioteka libsidplay
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplay.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê libsidplay.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub scripts/
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/libsidplay.so.*.*

%files devel
%defattr(644,root,root,755)
%doc DEVELOPER src/fastforward.txt src/format.txt src/mixing.txt src/mpu.txt src/panning.txt
%attr(755,root,root) %{_libdir}/libsidplay.so
%{_libdir}/libsidplay.la
%{_includedir}/sidplay

%files static
%defattr(644,root,root,755)
%{_libdir}/libsidplay.a
