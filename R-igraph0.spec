%global packname igraph0
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.5.7
Release:          1
Summary:          Network analysis and visualization, old, deprecated package
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5.7.tar.gz
Requires:         R-stats R-stats4 R-rgl R-tcltk R-RSQLite R-digest R-graph R-Matrix
%ifarch i586
Requires:         libgmp10 libxml2
BuildRequires:    libgmp10 libxml2
%endif
%ifarch x86_64
Requires:         lib64gmp10 libxml2
BuildRequires:    lib64gmp10 libxml2
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-stats4 R-rgl R-tcltk R-RSQLite R-digest R-graph R-Matrix

%description
Network analysis package, old, deprecated version.
igraph0 is the old version of the igraph package, kept alive
temporarily, for compatibility reasons. In this package,
vertices and edges are indexed from zero, whereas in ’igraph’,
starting from version 0.6, they are indexed from one. Please do
not use this package for new projects.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/html_library.license.terms
%doc %{rlibdir}/%{packname}/html_library.tcl
%doc %{rlibdir}/%{packname}/my_html_library.tcl
%doc %{rlibdir}/%{packname}/tkigraph_help
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/igraph.gif
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
