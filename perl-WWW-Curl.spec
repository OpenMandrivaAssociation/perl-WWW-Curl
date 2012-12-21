%define	modname	WWW-Curl
%define	modver	4.15

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	6

Summary:	Perl extension interface for libcurl
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/WWW/%{modname}-%{modver}.tar.gz

BuildRequires:	libcurl-devel
BuildRequires:	perl-devel


%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# yes, some tests are interactive. that's Evil.
# no point in running them, then: they'll be skipped
#%{__make} test < /dev/null

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/WWW
%{perl_vendorarch}/auto/WWW
%{_mandir}/*/*

%changelog
* Fri Dec 21 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.150.0-6
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 4.150.0-4mdv2012.0
+ Revision: 765805
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 4.150.0-3
+ Revision: 764329
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4.150.0-2
+ Revision: 667412
- mass rebuild

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.150.0-1mdv2011.0
+ Revision: 612272
- update to new version 4.15

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.140.0-1mdv2011.0
+ Revision: 596698
- update to 4.14

* Fri Sep 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.130.0-1mdv2011.0
+ Revision: 575597
- update to 4.13

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 4.120.0-4mdv2011.0
+ Revision: 564593
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.120.0-3mdv2011.0
+ Revision: 555309
- rebuild

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.120.0-1mdv2011.0
+ Revision: 551204
- update to 4.12

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.110.0-1mdv2010.1
+ Revision: 480739
- update to 4.11

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.90.0-1mdv2010.0
+ Revision: 408097
- rebuild using %%perl_convert_version

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.09-1mdv2010.0
+ Revision: 394090
- update to new version 4.09

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.08-1mdv2010.0
+ Revision: 393798
- update to new version 4.08

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.07-1mdv2010.0
+ Revision: 383547
- update to new version 4.07

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.06-1mdv2010.0
+ Revision: 370246
- update to new version 4.06

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.05-1mdv2009.0
+ Revision: 232105
- update to new version 4.05

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.04-1mdv2009.0
+ Revision: 227978
- update to new version 4.04

* Fri Jun 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.02-1mdv2009.0
+ Revision: 227420
- update to new version 4.02

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.00-1mdv2009.0
+ Revision: 194960
- update to new version 4.00

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.12-1mdv2008.1
+ Revision: 175993
- update to new version 3.12

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 3.02-6mdv2008.1
+ Revision: 152404
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 3.02-5mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 27 2007 Emmanuel Andry <eandry@mandriva.org> 3.02-5mdv2007.0
+ Revision: 114330
- rebuild for libcurl
- Import perl-WWW-Curl

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.02-4mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.02-3mdk
- rebuild

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.02-2mdk
- rebuilt against openssl-0.9.8a

* Tue Oct 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.02-1mdk
- First Mandriva release. Replaces perl-Curl-easy.

