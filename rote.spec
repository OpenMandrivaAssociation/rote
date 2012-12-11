%define	major 0
%define	libname		%mklibname %{name} %{major}
%define	libname_devel	%mklibname -d  %{name} %{major}

Summary:	Simple C library for VT102 terminal emulation
Name:		rote
Version:	0.2.8
Release:	7
License:	GPL
Group:		System/Libraries
Url:		http://rote.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(ncurses)

%description
ROTE is a simple C library for VT102 terminal emulation. It allows
the programmer to set up virtual 'screens' and send them data. The
virtual screens will emulate the behavior of a VT102 terminal,
interpreting escape sequences, control characters and such. The
library supports ncurses as well so that you may render the 
virtual screen to the real screen when you need to.

%package -n %{libname}
Summary:	Simple C library for VT102 terminal emulation
Group:		System/Libraries

%description -n %{libname}
ROTE is a simple C library for VT102 terminal emulation. It allows
the programmer to set up virtual 'screens' and send them data. The
virtual screens will emulate the behavior of a VT102 terminal,
interpreting escape sequences, control characters and such. The
library supports ncurses as well so that you may render the 
virtual screen to the real screen when you need to.

This package contains the runtime files needed for ROTE.

%package -n %{libname_devel}
Summary:	Simple C library for VT102 terminal emulation
Group:		System/Libraries
Provides:	librote-devel
Requires:	%{libname} = %{version}-%{release}

%description -n %{libname_devel}
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
%configure2_5x
%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/rote-config

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname_devel}
%{_libdir}/*.so
%{_includedir}/*
%{multiarch_bindir}/rote-config
%{_bindir}/rote-config

