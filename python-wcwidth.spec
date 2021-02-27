#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	wcwidth
Summary:	Measure the number of terminal column cells of wide-character codes
Summary(pl.UTF-8):	Pomiar liczby kolumn terminala koniecznych do wyświetlenia znaków
Name:		python-%{module}
Version:	0.1.8
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/jquast/wcwidth/releases
Source0:	https://github.com/jquast/wcwidth/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	66162542f776260ae611085ca92a97f1
URL:		https://pypi.org/project/wcwidth/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is mainly for those implementing a Terminal Emulator, or
programs that carefully produce output to be interpreted by one.

%description -l pl.UTF-8
Ta biblioteka przydaje się głównie implementującym emulator terminala
lub programom uważnie tworzących wyjście do interpretowania przez
takowy.

%package -n python3-%{module}
Summary:	Measure the number of terminal column cells of wide-character codes
Summary(pl.UTF-8):	Pomiar liczby kolumn terminala koniecznych do wyświetlenia znaków
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This library is mainly for those implementing a Terminal Emulator, or
programs that carefully produce output to be interpreted by one.

%description -n python3-%{module} -l pl.UTF-8
Ta biblioteka przydaje się głównie implementującym emulator terminala
lub programom uważnie tworzących wyjście do interpretowania przez
takowy.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest wcwidth/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest wcwidth/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/wcwidth/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/wcwidth/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/wcwidth
%{py_sitescriptdir}/wcwidth-0.1.7-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/wcwidth
%{py3_sitescriptdir}/wcwidth-0.1.7-py*.egg-info
%endif
