Summary:	PKCS#11 implementation of GnuPG Agent using the GnuPG Smart Card Daemon
Summary(pl.UTF-8):   Implementacja PKCS#11 Agenta GnuPG przy użyciu GnuPG Smart Card Daemona
Name:		scute
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/scute/%{name}-%{version}.tar.bz2
# Source0-md5:	1e5b495c801482b84933fff22b641959
Patch0:		%{name}-opt.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
# configure says 0.6.10, but assuan_set_assuan_err_source() needs 0.9.0
BuildRequires:	libassuan-devel >= 1:0.9.0
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libtool
Requires:	gnupg-smime >= 1.9.6
Requires:	libassuan >= 1:0.9.0
Requires:	libgpg-error >= 0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PKCS#11 implementation for the GnuPG Agent using the GnuPG
Smart Card Daemon. Currently, only the OpenPGP card is supported.

Scute enables you to use your OpenPGP smart card for client
authentication with SSL in Mozilla.

%description -l pl.UTF-8
To jest implementacja PKCS#11 Agenta GnuPG przy użyciu GnuPG Smart
Card Daemona. Aktualnie obsługiwane są tylko karty OpenPGP.

Scute pozwala używać kart procesorowych OpenPGP do uwierzytelniania
klientów przy użyciu SSL w Mozilli.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gpgsm=/usr/bin/gpgsm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libscute.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/website
%attr(755,root,root) %{_libdir}/libscute.so.*.*.*
%attr(755,root,root) %{_libdir}/libscute.so
