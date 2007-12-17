%define module		WWW-Curl
%define name		perl-%{module}
%define version		3.02
%define release		%mkrel 5

Summary:	Perl extension interface for libcurl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libcurl-devel
Obsoletes:	perl-Curl-easy
Provides:	perl-Curl-easy

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
# yes, some tests are interactive. that's Evil.
# no point in running them, then: they'll be skipped
#%{__make} test < /dev/null

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/WWW/*
%{perl_vendorarch}/auto/WWW/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT


