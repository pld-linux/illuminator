Summary:	Illuminator -
Summary(pl):	Illuminator -	
Name:		illuminator
Version:	1.0	
Release:	1
License:	GPL
Group:		Applications
Group(pl):	Aplikacje
Source0:	http://documents.cfar.umd.edu/ftp/pub/documents/contrib/sources/illuminator/illuminator-version.1.0/illum.src.tar.gz
Source1:	http://documents.cfar.umd.edu/ftp/pub/documents/contrib/sources/illuminator/illuminator-version.1.0/illum.doc.tar.gz
Patch0:		
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description


%description -l pl
#%description 
#%description -l pl
 # optional package ===================== #%package #Summary: #Summary(pl):
#Group: #Vesrion:   # end of optional package ==============

%prep
rm -rf %name-%version
mkdir %name-%version
cd %name-%version
gzip -dc %{SOURCE0} | tar -xf -


%build
cd %name-%version
cd src
make clean
make

#./configure --prefix=%{_prefix}
#make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
cd %name-%version/src
make prefix=$RPM_BUILD_ROOT%{_prefix}

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