
%define         _name

Summary:        KDE theme - %{_name}
Summary(pl):    Motyw KDE - %{_name}
Name:           kde-style-%{_name}
Version:        
Release:        1
License:        GPL
Group:          Themes
Source0:	%{_name}-%version}.tar.bz2
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
%{_theme} is

%description -l pl
%{_theme} to styl

%prep
%setup -q -n %{_name}-%{version}


%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc
