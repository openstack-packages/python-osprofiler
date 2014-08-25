%global pypi_name osprofiler

Name:           python-osprofiler
Version:        XXX
Release:        1%{?dist}
Summary:        OpenStack cross-project profiling library

License:        ASL 2.0
URL:            https://launchpad.net/osprofiler
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:	python-six
Requires:	python-webob

%description
OSProfiler is an OpenStack cross-project profiling library.

%prep
%setup -q -n osprofiler-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%dir %{python_sitelib}/osprofiler
%{python_sitelib}/osprofiler
%{python_sitelib}/osprofiler-%{version}*
%{_bindir}/osprofiler

%changelog
* Mon Aug 25 2014 Derek Higgins <derekh@redhat.com> - XXX
- Added dependencies on python-six and python-webob

* Fri Aug 15 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package.
