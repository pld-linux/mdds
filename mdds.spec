#
# Conditional build:
%bcond_without	apidocs	# doxygen/sphinx+breathe API documentation
#
Summary:	A collection of multi-dimensional data structures and indexing algorithms
Summary(pl.UTF-8):	Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących
Name:		mdds
Version:	1.5.0
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://gitlab.com/mdds/mdds/raw/master/README.md
Source0:	http://kohei.us/files/mdds/src/%{name}-%{version}.tar.bz2
# Source0-md5:	52cb08e92fec8842a3724bd89051f9d3
Patch0:		%{name}-doc.patch
URL:		https://gitlab.com/mdds/mdds
BuildRequires:	boost-devel >= 1.39
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.446
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	python3-breathe
BuildRequires:	sphinx-pdg-3
%endif
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
Requires:	libstdc++-devel >= 6:4.7

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

%package apidocs
Summary:	API documentation for MDDS
Summary(pl.UTF-8):	Dokumentacja API biblioteki MDDS
Group:		Documentation

%description apidocs
API documentation for MDDS.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki MDDS.

%prep
%setup -q

%build
%configure \
	SPHINX=/usr/bin/sphinx-build-3 \
	%{?with_apidocs:--enable-docs}

%{__make}

%if %{with apidocs}
%{__make} html-local
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mdds

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README.md
%{_includedir}/mdds-1.5
%{_npkgconfigdir}/mdds-1.5.pc

%files apidocs
%defattr(644,root,root,755)
%doc doc/_doxygen/html doc/_build/{_static,*.html,*.js}
