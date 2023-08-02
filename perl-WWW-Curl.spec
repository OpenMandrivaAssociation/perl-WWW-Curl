%define upstream_name WWW-Curl
%define upstream_version 4.17

%ifarch %{x86_64}
# Workaround for debugsource generator bug
%define _debugsource_template %{nil}
%endif

Summary:	Perl extension interface for libcurl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	12
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/pod/WWW::Curl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/perl-WWW-Curl/raw/rawhide/f/WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=941915
Patch1:		https://src.fedoraproject.org/rpms/perl-WWW-Curl/raw/rawhide/f/WWW-Curl-4.17-define-CURL-as-void.patch
# Adapt to changes in cURL 7.69.0, bug #1812910, CPAN RT#132197
Patch2:		https://src.fedoraproject.org/rpms/perl-WWW-Curl/raw/rawhide/f/WWW-Curl-4.17-Adapt-to-changes-in-cURL-7.69.0.patch
# Adapt to changes in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch3:		https://src.fedoraproject.org/rpms/perl-WWW-Curl/raw/rawhide/f/WWW-Curl-4.17-Adapt-to-curl-7.87.0.patch
# Workound a bug in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch4:		https://src.fedoraproject.org/rpms/perl-WWW-Curl/raw/rawhide/f/WWW-Curl-4.17-Work-around-a-macro-bug-in-curl-7.87.0.patch
# OM patches
# Adapt to changes in cURL 8.2.1
Patch100:	WWW-Curl-curl-8.2.1.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Install

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

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
