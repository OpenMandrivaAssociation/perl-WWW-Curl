%define upstream_name WWW-Curl
%define upstream_version 4.17

Summary:	Perl extension interface for libcurl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/pod/WWW::Curl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		perl-WWW-Curl-fix-CURL_STRICTER-undeclared.patch
Patch1:		WWW-Curl-4.17-RT117793-1.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=941915
Patch2:         WWW-Curl-4.17-define-CURL-as-void.patch
Patch3:		WWW-Curl-4.150.0-curl-7.50.2.patch
Patch4:		WWW-Curl-4.17-RT130591.patch
Patch5:		WWW-Curl-4.17-RT120736.patch
Patch6:		fixed-curlopt-udnef.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Install

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%autopatch -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# yes, some tests are interactive. that's Evil.
# no point in running them, then: they'll be skipped
# make test < /dev/null

%install
%make_install

%files
%doc README Changes
%{perl_vendorarch}/WWW
%{perl_vendorarch}/auto/WWW
%{_mandir}/*/*
