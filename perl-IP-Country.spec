%define upstream_name	 IP-Country
%define upstream_version 2.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Fast lookup of country codes from IP addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Geography::Countries)
BuildArch:	noarch

%description
IP lookup modules for Perl. This package also provides the ip2cc utility, to
lookup country from IP address or hostname.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/IP
%{_mandir}/*/*
%{_bindir}/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.270.0-4mdv2012.0
+ Revision: 765378
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.270.0-3
+ Revision: 763895
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.270.0-2
+ Revision: 667215
- mass rebuild

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 2.270.0-1mdv2010.1
+ Revision: 400644
- update to 2.27
- using %%perl_convert_version
- fixed license field

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-1mdv2009.1
+ Revision: 324506
- update to new version 2.26

* Fri Jun 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.25-1mdv2009.0
+ Revision: 229471
- update to new version 2.25

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.24-2mdv2009.0
+ Revision: 180414
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.24

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.23-1mdv2008.0
+ Revision: 20231
- 2.23


* Thu Apr 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.21-1mdk
- New release 2.21
- spec cleanup
- fix directory ownership
- %%mkrel
- better summary
- better source URL
- better buildrequires syntax

* Mon May 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.20-1mdk
- 2.20
- add tests, spec cleanup, rewrite description

* Mon Nov 15 2004 Austin Acton <austin@mandrake.org> 2.18-1mdk
- 2.18

* Sun Dec 14 2003 Abel Cheung <deaddog@deaddog.org> 2.17-1mdk
- 2.17

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.11-2mdk
- rebuild for new auto{prov,req}

