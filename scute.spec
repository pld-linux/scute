Summary:	PKCS#11 implementation of GnuPG Agent using the GnuPG Smart Card Daemon
Summary(pl.UTF-8):	Implementacja PKCS#11 Agenta GnuPG przy użyciu GnuPG Smart Card Daemona
Name:		scute
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/scute/%{name}-%{version}.tar.bz2
# Source0-md5:	e7142c94c0bbb12fbd9c04b35c09f52f
Patch0:		%{name}-info.patch
URL:		http://www.gnupg.org/
BuildRequires:	ImageMagick
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.14
BuildRequires:	libassuan-devel >= 1:2.5.0
BuildRequires:	libgpg-error-devel >= 1.24
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	texinfo
# epstopdf
BuildRequires:	texlive-pdftex
Requires(post,postun):	/sbin/ldconfig
Requires:	gnupg-smime >= 1.9.6
Requires:	libassuan >= 1:2.5.0
Requires:	libgpg-error >= 1.24
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gpg-agent=/usr/bin/gpg-agent \
	--with-gpg-connect-agent=/usr/bin/gpg-connect-agent \
	--with-gpgsm=/usr/bin/gpgsm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scute.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/website
%attr(755,root,root) %{_libdir}/scute.so
%{_infodir}/scute.info*
