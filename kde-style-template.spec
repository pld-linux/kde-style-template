
%define         _name

Summary:        KDE style - %{_name}
Summary(pl):    Styl do KDE - %{_name}
Name:           kde-style-%{_name}
Version:        
Release:        1
License:        GPL
Group:          Themes
Source0:	%{_name}-%{version}.tar.bz2
# Source0-md5:
URL:
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype-devel
BuildRequires:  kdelibs-devel
Requires:       kdelibs
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description 
%{_name} is

%description -l pl
%{_name} to styl

%prep
%setup -q -n %{_name}-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create dirs if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_datadir}/apps/kstyle/themes/*.themerc
