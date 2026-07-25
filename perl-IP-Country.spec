%define modname	IP-Country
%define modver 2.28

Summary:	Fast lookup of country codes from IP addresses
Name:		perl-%{modname}
Version:	%{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/IP-Country
Source0:	https://cpan.metacpan.org/authors/id/N/NW/NWETTERS/IP-Country-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl(Geography::Countries)

%description
IP lookup modules for Perl. This package also provides the ip2cc utility, to
lookup country from IP address or hostname.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/IP
%{_mandir}/man1/*
%{_mandir}/man3/*


