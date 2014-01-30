Summary:	A collection of multi-dimensional data structures and indexing algorithms
Summary(pl.UTF-8):	Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących
Name:		mdds
Version:	0.10.1
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: http://code.google.com/p/multidimalgorithm/wiki/Downloads
Source0:	http://kohei.us/files/mdds/src/%{name}_%{version}.tar.bz2
# Source0-md5:	01a380acfec23bf617117ce98e318f3d
URL:		http://code.google.com/p/multidimalgorithm/
BuildRequires:	autoconf >= 2.50
BuildRequires:	boost-devel >= 1.39
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	sed >= 4.0
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
Requires:	boost-devel >= 1.39

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

# this is only used in tests
sed -i -e '/^CPPFLAGS_NODEBUG/s/-Wall -Os -g/%{rpmcflags} -Wall/' configure.ac

%build
%{__autoconf}
# we can switch from boost to c++0x (the default) if sufficiently new C++11 compliant g++ is enforced
%configure \
	--with-hash-container=boost
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/mdds
cp -a include/mdds/* $RPM_BUILD_ROOT%{_includedir}/mdds
install -Dp misc/mdds.pc $RPM_BUILD_ROOT%{_npkgconfigdir}/mdds.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_includedir}/mdds
%{_npkgconfigdir}/mdds.pc
