%define modname	File-BaseDir
%define modver	0.08

Summary:	Perl module to use the freedesktop basedir spec
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes
%{perl_vendorlib}/File/*
%doc %{_mandir}/man3/*
