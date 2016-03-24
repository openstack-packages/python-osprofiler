# Created by pyp2rpm-1.1.0b
%global pypi_name osprofiler

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        OpenStack Profiler Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}%{?milestone}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires: python-six
Requires: python-webob

%description
OSProfiler is an OpenStack cross-project profiling library.


%package doc
Summary:    Documentation for the OpenStack Profiler Library
Group:      Documentation

BuildRequires:  python-sphinx

%description doc
Documentation for the OpenStack Profiler Library


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{_bindir}/osprofiler
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info

%files doc
%doc LICENSE html

%changelog
* Thu Mar 24 2016 RDO <rdo-list@redhat.com> 1.2.0-1
- RC1 Rebuild for Mitaka 
