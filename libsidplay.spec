Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl.UTF-8):	Biblioteka odtwarzająca muzyczki z Commodore 64 i emulująca układ SID
Name:		libsidplay
Version:	1.36.59
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tgz
# Source0-md5:	37c51ba4bd57164b1b0bb7b43b9adece
Patch0:		%{name}-gcc34.patch
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Group:		Libraries
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
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplay.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję libsidplay.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub scripts/
%{__libtoolize}
%{__aclocal}
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
