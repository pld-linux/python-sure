#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	sure
Summary:	Utility belt for automated testing in python for python
Name:		python-%{module}
Version:	1.2.12
Release:	1
License:	GPL v3+
Group:		Libraries/Python
# Source0:	https://github.com/gabrielfalcao/sure/archive/%{version}.tar.gz
Source0:	https://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	fc57c30e76bddba68f84443ec91e7026
URL:		https://github.com/gabrielfalcao/sure
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
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
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py_sitescriptdir}/sure
%{py_sitescriptdir}/sure/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc  README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
