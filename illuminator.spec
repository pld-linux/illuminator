Summary:	Illuminator -
Summary(pl):	Illuminator -
Name:		illuminator
Version:	1.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.cfar.umd.edu/pub/documents/contrib/sources/illuminator/illuminator-version.1.0/illum.src.tar.gz
Source1:	ftp://ftp.cfar.umd.edu/pub/documents/contrib/sources/illuminator/illuminator-version.1.0/illum.doc.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
cd src
%{__make} clean
%{__make}

#./configure --prefix=%{_prefix}
#make RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix}

#make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
#rm -rf $RPM_BUILD_ROOT
#rm -rf $RPM_BUILD_DIR/%name-%version

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)

# optional package

#%files
%defattr(644,root,root,755)
#%doc
#%attr(,,)
#end of optional package
