Summary:	A collection of multi-dimensional data structures and indexing algorithms
Summary(pl.UTF-8):	Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących
Name:		mdds
Version:	0.6.0
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://code.google.com/p/multidimalgorithm/downloads/list
Source0:	http://multidimalgorithm.googlecode.com/files/%{name}_%{version}.tar.bz2
# Source0-md5:	3e89a35f253a4f1c7de68c57d851ef38
Patch0:		0001-Fixes-build-breakage-on-Debian.patch
Patch1:		0001-fix-linking-error-with-boost-1.50.patch
Patch2:		0001-help-compiler-select-the-right-overload-of-vector-in.patch
URL:		http://code.google.com/p/multidimalgorithm/
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

%description -l pl.UTF-8
Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących.
Zaimplementowane są następujące struktury danych:
- drzewo segmentowe
- płaskie drzewo segmentowe
- zbiór prostokątów
- drzewo czwórkowe (quadtree) dla punktów
- macierz mieszana

%package devel
Summary:	A collection of multi-dimensional data structures and indexing algorithms
Summary(pl.UTF-8):	Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących
Group:		Development/Libraries
Requires:	boost-devel

%description devel
A collection of multi-dimensional data structures and indexing
algorithms.

It implements the following data structures:
- segment tree
- flat segment tree
- rectangle set
- point quad tree
- mixed type matrix

%description devel -l pl.UTF-8
Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących.
Zaimplementowane są następujące struktury danych:
- drzewo segmentowe
- płaskie drzewo segmentowe
- zbiór prostokątów
- drzewo czwórkowe (quadtree) dla punktów
- macierz mieszana

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# this is only used in tests
sed -i -e '/^CPPFLAGS/s/-Wall.*-std/%{rpmcflags} -std/' Makefile.in

%build
# we can switch from boost to c++0x (the default) if sufficiently new C++11 compliant g++ is enforced
%configure \
	--with-hash-container=boost
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
