#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compositeproto
Version  : 0.4.2
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/proto/compositeproto-0.4.2.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/compositeproto-0.4.2.tar.bz2
Summary  : Composite extension headers
Group    : Development/Tools
License  : MIT
Requires: compositeproto-doc
BuildRequires : pkgconfig(xorg-macros)

%description
Composite Extension
Version 0.1
2003-11-04
This package contains header files and documentation for the composite
extension.  Library and server implementations are separate.

%package dev
Summary: dev components for the compositeproto package.
Group: Development

%description dev
dev components for the compositeproto package.


%package doc
Summary: doc components for the compositeproto package.
Group: Documentation

%description doc
doc components for the compositeproto package.


%prep
%setup -q -n compositeproto-0.4.2

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/composite.h
/usr/include/X11/extensions/compositeproto.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/compositeproto/*
