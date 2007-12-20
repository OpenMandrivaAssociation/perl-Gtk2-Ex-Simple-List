%define	module	Gtk2-Ex-Simple-List
%define	name	perl-%{module}
%define	version	0.50
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A simple interface to Gtk2's complex MVC list widget
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-Gtk2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/Gtk2

