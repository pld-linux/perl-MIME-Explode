#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Explode
Summary:	MIME::Explode - Perl extension for explode MIME messages
Summary(pl):	MIME::Explode - rozszerzenie Perla do rozbijania wiadomo¶ci MIME
Name:		perl-MIME-Explode
Version:	0.28
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7a0405bc81489298bf3881cad973b28e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Explode is Perl module for parsing and decoding single or
multipart MIME messages, and outputting its decoded components to a
given directory. This module is designed to allows users to extract
the attached files out of a MIME encoded email messages or mailboxes.

%description -l pl
MIME::Explode to modu³ Perla do analizy i dekodowania jedno- i
wieloczê¶ciowych wiadomo¶ci MIME oraz zapisu zdekodowanych sk³adników
do podanego katalogu. Ten modu³ zosta³ opracowany aby umo¿liwiæ
u¿ytkownikom wydobywanie za³±czników z zakodowanych MIME wiadomo¶ci
lub skrzynek pocztowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/MIME/Explode/Explode.bs
%attr(755,root,root) %{perl_vendorarch}/auto/MIME/Explode/Explode.so
%{_mandir}/man3/*
