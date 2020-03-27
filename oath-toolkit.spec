#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x860B7FBB32F8119D (simon@yubico.com)
#
Name     : oath-toolkit
Version  : 2.6.2
Release  : 3
URL      : http://download.savannah.nongnu.org/releases/oath-toolkit/oath-toolkit-2.6.2.tar.gz
Source0  : http://download.savannah.nongnu.org/releases/oath-toolkit/oath-toolkit-2.6.2.tar.gz
Source99 : http://download.savannah.nongnu.org/releases/oath-toolkit/oath-toolkit-2.6.2.tar.gz.sig
Summary  : Library for Portable Symmetric Key Container
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.1 LGPL-2.1+
Requires: oath-toolkit-bin = %{version}-%{release}
Requires: oath-toolkit-lib = %{version}-%{release}
Requires: oath-toolkit-license = %{version}-%{release}
Requires: oath-toolkit-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(xmlsec1)
BuildRequires : valgrind
Patch1: 0001-Update-gnulib-files.patch
Patch2: 0002-Fix-build-with-glibc-2.18.patch

%description
The OATH Toolkit makes it easy to build one-time password
authentication systems.  It contains shared libraries, command line
tools and a PAM module.  Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238).  OATH stands for Open AuTHentication, which is the
organization that specify the algorithms.  For managing secret key
files, the Portable Symmetric Key Container (PSKC) format described in
RFC6030 is supported.

%package bin
Summary: bin components for the oath-toolkit package.
Group: Binaries
Requires: oath-toolkit-license = %{version}-%{release}
Requires: oath-toolkit-man = %{version}-%{release}

%description bin
bin components for the oath-toolkit package.


%package dev
Summary: dev components for the oath-toolkit package.
Group: Development
Requires: oath-toolkit-lib = %{version}-%{release}
Requires: oath-toolkit-bin = %{version}-%{release}
Provides: oath-toolkit-devel = %{version}-%{release}

%description dev
dev components for the oath-toolkit package.


%package doc
Summary: doc components for the oath-toolkit package.
Group: Documentation
Requires: oath-toolkit-man = %{version}-%{release}

%description doc
doc components for the oath-toolkit package.


%package lib
Summary: lib components for the oath-toolkit package.
Group: Libraries
Requires: oath-toolkit-license = %{version}-%{release}

%description lib
lib components for the oath-toolkit package.


%package license
Summary: license components for the oath-toolkit package.
Group: Default

%description license
license components for the oath-toolkit package.


%package man
Summary: man components for the oath-toolkit package.
Group: Default

%description man
man components for the oath-toolkit package.


%prep
%setup -q -n oath-toolkit-2.6.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538722370
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1538722370
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oath-toolkit
cp COPYING %{buildroot}/usr/share/package-licenses/oath-toolkit/COPYING
cp liboath/COPYING %{buildroot}/usr/share/package-licenses/oath-toolkit/liboath_COPYING
cp oathtool/COPYING %{buildroot}/usr/share/package-licenses/oath-toolkit/oathtool_COPYING
cp pam_oath/COPYING %{buildroot}/usr/share/package-licenses/oath-toolkit/pam_oath_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oathtool

%files dev
%defattr(-,root,root,-)
/usr/include/liboath/oath.h
/usr/lib64/liboath.so
/usr/lib64/pkgconfig/liboath.pc
/usr/share/man/man3/oath_authenticate_usersfile.3
/usr/share/man/man3/oath_base32_decode.3
/usr/share/man/man3/oath_base32_encode.3
/usr/share/man/man3/oath_bin2hex.3
/usr/share/man/man3/oath_check_version.3
/usr/share/man/man3/oath_done.3
/usr/share/man/man3/oath_hex2bin.3
/usr/share/man/man3/oath_hotp_generate.3
/usr/share/man/man3/oath_hotp_validate.3
/usr/share/man/man3/oath_hotp_validate_callback.3
/usr/share/man/man3/oath_init.3
/usr/share/man/man3/oath_strerror.3
/usr/share/man/man3/oath_strerror_name.3
/usr/share/man/man3/oath_totp_generate.3
/usr/share/man/man3/oath_totp_generate2.3
/usr/share/man/man3/oath_totp_validate.3
/usr/share/man/man3/oath_totp_validate2.3
/usr/share/man/man3/oath_totp_validate2_callback.3
/usr/share/man/man3/oath_totp_validate3.3
/usr/share/man/man3/oath_totp_validate3_callback.3
/usr/share/man/man3/oath_totp_validate4.3
/usr/share/man/man3/oath_totp_validate4_callback.3
/usr/share/man/man3/oath_totp_validate_callback.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/liboath/api-index-1-10-0.html
/usr/share/gtk-doc/html/liboath/api-index-1-12-0.html
/usr/share/gtk-doc/html/liboath/api-index-1-4-0.html
/usr/share/gtk-doc/html/liboath/api-index-1-6-0.html
/usr/share/gtk-doc/html/liboath/api-index-1-8-0.html
/usr/share/gtk-doc/html/liboath/api-index-2-4-0.html
/usr/share/gtk-doc/html/liboath/api-index-2-6-0.html
/usr/share/gtk-doc/html/liboath/api-index-full.html
/usr/share/gtk-doc/html/liboath/home.png
/usr/share/gtk-doc/html/liboath/index.html
/usr/share/gtk-doc/html/liboath/index.sgml
/usr/share/gtk-doc/html/liboath/intro.html
/usr/share/gtk-doc/html/liboath/left-insensitive.png
/usr/share/gtk-doc/html/liboath/left.png
/usr/share/gtk-doc/html/liboath/liboath-oath.html
/usr/share/gtk-doc/html/liboath/liboath.devhelp2
/usr/share/gtk-doc/html/liboath/right-insensitive.png
/usr/share/gtk-doc/html/liboath/right.png
/usr/share/gtk-doc/html/liboath/style.css
/usr/share/gtk-doc/html/liboath/up-insensitive.png
/usr/share/gtk-doc/html/liboath/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib/security/pam_oath.so
/usr/lib64/liboath.so.0
/usr/lib64/liboath.so.0.1.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oath-toolkit/COPYING
/usr/share/package-licenses/oath-toolkit/liboath_COPYING
/usr/share/package-licenses/oath-toolkit/oathtool_COPYING
/usr/share/package-licenses/oath-toolkit/pam_oath_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/oathtool.1
