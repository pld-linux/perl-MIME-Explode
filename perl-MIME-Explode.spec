#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	MIME
%define		pnam	Explode
Summary:	MIME::Explode - Perl extension for explode MIME messages
Summary(pl.UTF-8):	MIME::Explode - rozszerzenie Perla do rozbijania wiadomości MIME
Name:		perl-MIME-Explode
Version:	0.39
Release:	17
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	87be0487497ee30b4566ceac2dbaf733
URL:		http://search.cpan.org/dist/MIME-Explode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Explode is Perl module for parsing and decoding single or
multipart MIME messages, and outputting its decoded components to a
given directory. This module is designed to allows users to extract
the attached files out of a MIME encoded email messages or mailboxes.

%description -l pl.UTF-8
MIME::Explode to moduł Perla do analizy i dekodowania jedno- i
wieloczęściowych wiadomości MIME oraz zapisu zdekodowanych składników
do podanego katalogu. Ten moduł został opracowany aby umożliwić
użytkownikom wydobywanie załączników z zakodowanych MIME wiadomości
lub skrzynek pocztowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/MIME/Explode.pm
%dir %{perl_vendorarch}/auto/MIME/Explode
%{perl_vendorarch}/auto/MIME/Explode/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/MIME/Explode/Explode.so
%{_mandir}/man3/*
