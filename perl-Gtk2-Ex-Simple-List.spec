%define	upstream_name	 Gtk2-Ex-Simple-List
%define	upstream_version 0.50

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A simple interface to Gtk2's complex MVC list widget
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Gtk2)
BuildArch:	noarch

%description
Gtk2 has a powerful, but complex MVC (Model, View, Controller) system used to
implement list and tree widgets. Gtk2::Ex::Simple::List automates the complex
setup work and allows you to treat the list model as a more natural list of
lists structure.

After creating a new Gtk2::Ex::Simple::List object with the desired columns you
may set the list data with a simple Perl array assignment. Rows may be added or
deleted with all of the normal array operations. You can treat the data member
of the Simple::List object as an array reference, and manipulate the list data
with perl's normal array operators.

A mechanism has also been put into place allowing columns to be Perl scalars.
The scalar is converted to text through Perl's normal mechanisms and then
displayed in the list. This same mechanism can be expanded by defining
arbitrary new column types before calling the new function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/Gtk2


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 403229
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.50-6mdv2009.0
+ Revision: 257146
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-4mdv2008.1
+ Revision: 133633
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-3mdv2007.0
- Rebuild

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-2mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdk
- first mdk release

