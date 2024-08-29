#
# Conditional build:
%bcond_without	apidocs	# doxygen/sphinx+breathe API documentation
#
Summary:	A collection of multi-dimensional data structures and indexing algorithms
Summary(pl.UTF-8):	Zbiór struktur danych wielowymiarowych oraz algorytmów indeksujących
Name:		mdds
# keep in sync with BuildRequires in libreoffice.spec, ixion.spec, liborcus.spec
Version:	2.1.1
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://gitlab.com/mdds/mdds/-/releases
Source0:	https://kohei.us/files/mdds/src/%{name}-%{version}.tar.xz
# Source0-md5:	4d8ac3838997525e2dc748e8e34c3015
Patch0:		%{name}-doc.patch
URL:		https://gitlab.com/mdds/mdds
BuildRequires:	boost-devel >= 1.39
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Requires:	libstdc++-devel >= 6:7

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
%{__make} -j1 doc
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
%{_includedir}/mdds-2.1
%{_npkgconfigdir}/mdds-2.1.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_doxygen/html doc/_build/{_static,*.html,*.js}
%endif
