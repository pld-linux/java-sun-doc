Summary:	Java(TM) 2 SDK documentation
Summary(pl):	Dokumentacja do Java(TM) 2 SDK
Name:		java-sun-doc
Version:	1.5
Release:	1
License:	non-distributable (see license.html and http://java.sun.com/docs/redist.html)
Group:		Documentation
# download through forms from http://java.sun.com/j2se/1.5.0/download.jsp
Source0:	jdk-1_5_0-doc.zip
# NoSource0-md5: 06d108655466460e12bc9018c5fee863
URL:		http://java.sun.com/linux/
NoSource:	0
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java(TM) 2 SDK documentation for language, API, tools, demos etc.

%description -l pl
Dokumentacja do Java(TM) 2 SDK - do jêzyka, API, narzêdzi, programów
demonstracyjnych i innych.

%prep
%setup -q -n docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/j2sdk

cp -rf * $RPM_BUILD_ROOT%{_docdir}/j2sdk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/j2sdk
