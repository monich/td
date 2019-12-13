Name: tdlib
Summary: Cross-platform library for building Telegram clients
Version: 1.8.67
Release: 0
Group:   Development/Libraries
License: BSL-1.0
URL:     https://github.com/monich/td
Source: %{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: gperf
BuildRequires: openssl-devel

%define _binary_payload w6.xzdio
%{!?make_build:%define make_build make %{_smp_mflags}}

%description
%{summary}.

%package devel
Summary:    Development files for Telegram TD library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q

%build

SOURCE_DIR=`pwd`

mkdir -p build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} $SOURCE_DIR
%make_build %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libtd*.so.*

%files devel
%dir %{_includedir}/td
%dir %{_includedir}/td/tl
%dir %{_includedir}/td/telegram
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Td
%{_includedir}/td/telegram/*.h
%{_includedir}/td/telegram/*.hpp
%{_includedir}/td/tl/*.h
%{_libdir}/cmake/Td/*.cmake
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libtd*.so
%{_libdir}/libtd*.a
