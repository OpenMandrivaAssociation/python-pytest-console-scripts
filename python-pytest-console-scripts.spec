%define module pytest-console-scripts
%define oname pytest_console_scripts
%bcond tests 1

Name:		python-pytest-console-scripts
Version:	1.4.1
Release:	1
Summary:	Pytest plugin for testing console scripts
License:	MIT
Group:		Development/Python
URL:		https://github.com/kvas-it/pytest-console-scripts
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(virtualenv)

%description
Pytest plugin for testing console scripts.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%install -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%if %{with tests}
%check
sed -i 's|env python|python|' tests/test_run_scripts.py
export CI=true
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_console_scripts \
PYTHONPATH="%{buildroot}%{python_sitelib}" \
pytest -W ignore::DeprecationWarning --deselect tests/test_run_scripts.py::test_mocking[inprocess]
%endif

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*.*-info
