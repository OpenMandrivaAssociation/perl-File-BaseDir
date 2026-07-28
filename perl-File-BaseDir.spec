%define modname	File-BaseDir
%define modver	0.09

Summary:	Perl module to use the freedesktop basedir spec
Name:		perl-%{modname}
Version:	%{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/uperl/File-BaseDir
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-BaseDir-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(IPC::System::Simple)
BuildRequires:	perl(File::Which)

%description
Perl module to use the freedesktop basedir spec.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File/*
%doc %{_mandir}/man3/*
