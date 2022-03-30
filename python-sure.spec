#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		sure
Summary:	Utility belt for automated testing in Python for Python
Summary(pl.UTF-8):	Narzędzia do automatycznego testowania w Pythonie
Name:		python-%{module}
Version:	1.4.11
Release:	4
License:	GPL v3+
Group:		Libraries/Python
#Source0Download; https://pypi.org/simple/sure/
Source0:	https://files.pythonhosted.org/packages/source/s/sure/%{module}-%{version}.tar.gz
# Source0-md5:	51f28b4ea7a6f59d1dd09f8eaaeabee7
Patch0:		%{name}-mock.patch
URL:		https://github.com/gabrielfalcao/sure
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	python-six >= 1.10.0
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-nose
BuildRequires:	python3-setuptools
BuildRequires:	python3-six >= 1.10.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A testing library for Python with powerful and flexible assertions.
Sure is heavily inspired by should.js.

%description -l pl.UTF-8
Biblioteka testów dla Pythona z bardzo elastycznymi asercjami. Sure
jest znacząco zainspirowany should.js.

%package -n python3-%{module}
Summary:	Utility belt for automated testing in python for python
Summary(pl.UTF-8):	Narzędzia do automatycznego testowania w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
A testing library for Python with powerful and flexible assertions.
Sure is heavily inspired by should.js.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka testów dla Pythona z bardzo elastycznymi asercjami. Sure
jest znacząco zainspirowany should.js.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

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
%doc README.rst
%{py_sitescriptdir}/sure
%{py_sitescriptdir}/sure-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sure
%{py3_sitescriptdir}/sure-%{version}-py*.egg-info
%endif
