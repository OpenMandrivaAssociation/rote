%define major 0
%define name rote
%define version 0.2.8 
%define release %mkrel 5
%define  libname %mklibname %{name} %{major}
%define  libname_devel  %mklibname -d  %{name} %{major}


Summary: Simple C library for VT102 terminal emulation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Libraries
Url: http://rote.sourceforge.net/
BuildRequires: ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ROTE is a simple C library for VT102 terminal emulation. It allows
the programmer to set up virtual 'screens' and send them data. The
virtual screens will emulate the behavior of a VT102 terminal,
interpreting escape sequences, control characters and such. The
library supports ncurses as well so that you may render the 
virtual screen to the real screen when you need to.


%package -n %libname
Summary: Simple C library for VT102 terminal emulation
Group: System/Libraries

Provides: %{name}
Obsoletes: %{name}

%description -n %libname
ROTE is a simple C library for VT102 terminal emulation. It allows
the programmer to set up virtual 'screens' and send them data. The
virtual screens will emulate the behavior of a VT102 terminal,
interpreting escape sequences, control characters and such. The
library supports ncurses as well so that you may render the 
virtual screen to the real screen when you need to.

This package contains the runtime files needed for ROTE.
%package -n %libname_devel
Summary: Simple C library for VT102 terminal emulation
Group: System/Libraries
Provides: librote-devel
Requires: %libname = %{version}

%description -n %libname_devel
ROTE is a simple C library for VT102 terminal emulation. It allows
the programmer to set up virtual 'screens' and send them data. The
virtual screens will emulate the behavior of a VT102 terminal,
interpreting escape sequences, control characters and such. The
library supports ncurses as well so that you may render the 
virtual screen to the real screen when you need to.

This package contains the developement files needed for ROTE.
%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/rote-config

%clean
rm -rf $RPM_BUILD_ROOT


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libname_devel 
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%multiarch %{multiarch_bindir}/rote-config
%{_bindir}/rote-config

