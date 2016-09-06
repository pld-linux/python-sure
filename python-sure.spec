#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		sure
%define		egg_name	sure
%define		pypi_name	sure
Summary:	Utility belt for automated testing in Python for Python
Name:		python-%{module}
Version:	1.2.24
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a396cc3c71d551bfdb9bc45363ca05da
URL:		https://github.com/gabrielfalcao/sure
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-mock
BuildRequires:	python-nose
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-mock
BuildRequires:	python3-modules
BuildRequires:	python3-nose
BuildRequires:	python3-six
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A testing library for python with powerful and flexible assertions.
Sure is heavily inspired by should.js.

%package -n python3-%{module}
Summary:	Utility belt for automated testing in python for python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
A testing library for python with powerful and flexible assertions.
Sure is heavily inspired by should.js.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc  README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
