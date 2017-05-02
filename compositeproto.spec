#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compositeproto
Version  : 0.4.2
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/proto/compositeproto-0.4.2.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/compositeproto-0.4.2.tar.bz2
Summary  : Composite extension headers
Group    : Development/Tools
License  : MIT
Requires: compositeproto-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
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
Provides: compositeproto-devel

%description dev
dev components for the compositeproto package.


%package dev32
Summary: dev32 components for the compositeproto package.
Group: Default

%description dev32
dev32 components for the compositeproto package.


%package doc
Summary: doc components for the compositeproto package.
Group: Documentation

%description doc
doc components for the compositeproto package.


%prep
%setup -q -n compositeproto-0.4.2
pushd ..
cp -a compositeproto-0.4.2 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/composite.h
/usr/include/X11/extensions/compositeproto.h
/usr/lib64/pkgconfig/compositeproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32compositeproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/compositeproto/*
