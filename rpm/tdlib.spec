Name: tdlib
Summary: Cross-platform library for building Telegram clients
Version: 1.6.0
Release: 0
Group:   Development/Libraries
License: BSL-1.0
URL:     https://github.com/monich/td
Source: %{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: gperf
BuildRequires: openssl-devel

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

mkdir -p %{builddir}/build
cd %{builddir}/build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} $SOURCE_DIR

make %{?_smp_mflags}

%install
cd %{builddir}/build
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libtd*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/td
%dir %{_includedir}/td/tl
%dir %{_includedir}/td/telegram
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Td
%{_includedir}/td/telegram/*.h
%{_includedir}/td/telegram/*.hpp
%{_includedir}/td/tl/*.h
%{_libdir}/cmake/Td/*.cmake
%{_libdir}/libtd*.so
%{_libdir}/libtd*.a
