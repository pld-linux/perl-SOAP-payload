#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SOAP
%define		pnam	payload
Summary:	SOAP::payload - send various forms of information as SOAP envelopes
Summary(pl):	SOAP::payload - wysy³anie ró¿nych form informacji jako opakowañ SOAP
Name:		perl-SOAP-payload
Version:	1.02
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f55388ab1c1b630733259db463fffc5f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used in conjunction with other modules such as DBI,
to send data elements as part of a SOAP transaction envelope.

%description -l pl
Tego modu³u mo¿na u¿ywaæ wraz z innymi modu³ami takimi jak DBI do
wysy³ania danych jako czê¶ci opakowania transakcji SOAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

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
%{perl_vendorlib}/SOAP/payload.pm
%{_mandir}/man3/*
