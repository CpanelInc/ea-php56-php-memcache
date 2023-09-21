%global scl_version ea-php56
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcache
Version: 2.2.7
Summary: memcache extension for %{scl_version}
%define release_prefix 6
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcache
Source: https://pecl.php.net/get/memcache-2.2.7.tgz
Source1: memcache.ini

# should be no requires for building this package
#Requires: memcached
#BuildRequires: libyaml-devel
Requires: %{scl_version}-php-common
Requires: %{scl_version}-php-cli
BuildRequires: %{scl_version}

%description
Memcached is a caching daemon designed especially for  dynamic web applications
to decrease database load by storing objects in memory. This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -n memcache-%{version}

%build
scl enable %{scl_version} phpize
scl enable %{scl_version} ./configure
make

%install
#scl enable %{scl_version} 'make install DESTDIR=$RPM_BUILD_ROOT'
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcache.so
%config /%{ext_prefix}/%{conf_dir}/memcache.ini

%changelog
* Thu Sep 21 2023 Dan Muey <dan@cpanel.net> - 2.2.7-6
- ZC-11194: Remove unnecessary `BuildRequires` of php-cli

* Tue Dec 28 2021 Dan Muey <dan@cpanel.net> - 2.2.7-5
- ZC-9589: Update DISABLE_BUILD to match OBS

* Mon Apr 20 2020 Daniel Muey <dan@cpanel.net> - 2.2.7-4
- ZC-6608: Fix Requires for PHP

* Mon Apr 13 2020 Tim Mullin <tim@cpanel.net> - 2.2.7-3
- EA-8978: Add php as a dependency

* Wed Apr 08 2020 Daniel Muey <dan@cpanel.net> - 2.2.7-2
- ZC-6515: Promote from experimental

* Fri Mar  5 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- Fixed package name, entire RPM is now working.

* Wed Mar  1 2017 Jack Hayhurst <jack@deleteos.com> - 0.1
- Initial spec file creation.
