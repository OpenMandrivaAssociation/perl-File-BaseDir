%define module 	File-BaseDir
%define version 0.03
%define release %mkrel 4

Summary:	Perl module to use the freedesktop basedir spec
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
Perl module to use the freedesktop basedir spec.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File/*
%{_mandir}/*/*


