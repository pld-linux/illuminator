Summary:	Illuminator - viewer and editor for files in the DAFS format
Summary(pl.UTF-8):   Illuminator - przeglądarka i edytor plików w formacie DAFS
Name:		illuminator
Version:	1.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.cfar.umd.edu/pub/documents/contrib/sources/%{name}/%{name}-version.%{version}/illum.src.tar.gz
# Source0-md5:	eee2d8d4994f3b564ca20762c0db3f38
Source1:	ftp://ftp.cfar.umd.edu/pub/documents/contrib/sources/%{name}/%{name}-version.%{version}/illum.doc.tar.gz
# Source1-md5:	d9fab8e90266f29277a32a84b6bd80e7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Illuminator (illum) is the Motif/X11 viewer and editor for files in the
DAFS format.

%description -l pl.UTF-8
Illuminator (illum) jest korzystającą z Motif/X11 przeglądarką i edytorem
plików w formacie DAFS.

%prep
%setup -q -T -c -a0 -a1

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
