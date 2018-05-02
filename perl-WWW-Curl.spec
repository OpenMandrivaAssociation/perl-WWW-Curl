%define	modname	WWW-Curl
%define modver 4.17

Summary:	Perl extension interface for libcurl

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/WWW/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:  perl(Module::Install)

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# yes, some tests are interactive. that's Evil.
# no point in running them, then: they'll be skipped
#make test < /dev/null

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/WWW
%{perl_vendorarch}/auto/WWW
%{_mandir}/man3/*


