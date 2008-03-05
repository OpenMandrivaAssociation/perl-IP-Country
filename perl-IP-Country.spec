%define module	IP-Country
%define name	perl-%{module}
%define version	2.24
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Fast lookup of country codes from IP addresses
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IP/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Geography::Countries)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
IP lookup modules for Perl. This package also provides the ip2cc utility, to
lookup country from IP address or hostname.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/IP
%{_mandir}/*/*
%{_bindir}/*

