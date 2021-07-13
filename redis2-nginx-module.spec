#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redis2-nginx-module
Version  : 0.15
Release  : 19
URL      : https://github.com/openresty/redis2-nginx-module/archive/v0.15.tar.gz
Source0  : https://github.com/openresty/redis2-nginx-module/archive/v0.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: redis2-nginx-module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
Name
====
ngx_redis2 - Nginx upstream module for the Redis 2.0 protocol
*This module is not distributed with the Nginx source.* See [the installation instructions](#installation).

%package lib
Summary: lib components for the redis2-nginx-module package.
Group: Libraries

%description lib
lib components for the redis2-nginx-module package.


%prep
%setup -q -n redis2-nginx-module-0.15
cd %{_builddir}/redis2-nginx-module-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_redis2_module.so
