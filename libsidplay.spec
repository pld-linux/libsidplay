Name:		libsidplay
Summary:	A Commodore 64 music player and SID chip emulator library.
Version:	1.36.57
Release:	1
Group:		Libraries
License:	GPL
Source0:	http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tgz
URL:		http://www.geocities.com/SiliconValley/Lakes/5147/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it you
can play musics from Commodore 64 (or compatible) programs.

%package -n libsidplay-devel
Summary:	Header files for compiling apps that use libsidplay.
Group:		Libraries

%description -n libsidplay-devel
This package contains the header files for compiling applications that
use libsidplay.

%package -n libsidplay-static
Summary:	Static files for libsidplay.
Group:		Libraries

%description -n libsidplay-static
This package contains static files of libsidplay.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libsidplay.so*

%files -n libsidplay-devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING DEVELOPER
%doc src/fastforward.txt src/format.txt src/mixing.txt src/mpu.txt src/panning.txt
%{_includedir}/sidplay
%{_libdir}/libsidplay.la

%files -n libsidplay-static
%defattr(644,root,root,755)
%{_libdir}/libsidplay.a
