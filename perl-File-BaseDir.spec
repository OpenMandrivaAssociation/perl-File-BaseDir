%define upstream_name 	 File-BaseDir
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl module to use the freedesktop basedir spec
License:	GPL+ or Artistic
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to use the freedesktop basedir spec.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-4mdv2012.0
+ Revision: 765236
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-2
+ Revision: 667136
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 405963
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.03-4mdv2009.1
+ Revision: 351741
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.03-3mdv2009.1
+ Revision: 351735
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 223718
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.1
+ Revision: 105342
- new version


* Fri Sep 01 2006 Michael Scherer <misc@mandriva.org> 0.02-3mdv2007.0
- Rebuild

* Wed Aug 24 2005 Michael Scherer <misc@mandriva.org> 0.02-2mdk
- Birthday rebuild
- mkrel

* Mon Aug 23 2004 Michael Scherer <misc@mandrake.org> 0.02-1mdk 
- First Mandrakelinux package

