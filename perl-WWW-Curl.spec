%define module		WWW-Curl
%define name		perl-%{module}
%define version		4.02
%define release		%mkrel 1

Summary:	Perl extension interface for libcurl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	libcurl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
# yes, some tests are interactive. that's Evil.
# no point in running them, then: they'll be skipped
#%{__make} test < /dev/null

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/WWW
%{perl_vendorarch}/auto/WWW
%{_mandir}/*/*

