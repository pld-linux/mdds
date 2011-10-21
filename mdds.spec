Summary:	A collection of multi-dimensional data structures and indexing algorithms
Name:		mdds
Version:	0.5.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		http://code.google.com/p/multidimalgorithm/
Source0:	http://multidimalgorithm.googlecode.com/files/%{name}_%{version}.tar.bz2
# Source0-md5:	0ff7d225d087793c8c2c680d77aac3e7
BuildRequires:	boost-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of multi-dimensional data structures and indexing
algorithms.

It implements the following data structures:
- segment tree
- flat segment tree
- rectangle set
- point quad tree
- mixed type matrix

%package devel
Summary:	Headers for %{name}
Group:		Development/Libraries
Requires:	boost-devel

%description devel
Headers for %{name}.

%prep
%setup -q -n %{name}_%{version}
# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall.*-std/%{rpmcflags} -std/' Makefile.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/mdds
cp -a include/mdds/* $RPM_BUILD_ROOT%{_includedir}/mdds

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_includedir}/mdds
