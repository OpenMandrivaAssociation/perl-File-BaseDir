%define module 	File-BaseDir
%define version 0.02
%define release %mkrel 3

Summary:	Perl module to use the freedesktop basedir spec
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PARDUS/%{module}/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
Perl module to use the freedesktop basedir spec.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File/*
%{_mandir}/*/*


