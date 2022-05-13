# TODO: GTK4 variant for GNOME42 (--with-gtk4, requires libnma-gtk4 >= 1.8.33)
Summary:	NetworkManager VPN integration for SSTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem SSTP
Name:		NetworkManager-sstp
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-sstp/1.3/%{name}-%{version}.tar.xz
# Source0-md5:	5af9156712d809bb280f925da8da480c
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.7.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.7.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	gnutls-devel >= 2.12
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.4.9
BuildRequires:	sstp-client-devel >= 1.0.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.7.0
Requires:	NetworkManager-gtk-lib >= 1.7.0
Requires:	glib2 >= 1:2.40
Requires:	gtk+3 >= 3.4
Requires:	libsecret >= 0.18
%requires_eq_to	ppp ppp-plugin-devel
Requires:	sstp-client >= 1.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for SSTP.

%description -l pl.UTF-8
Integracja NetworkManagera z protokołem SSTP.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins \
	--without-libnm-glib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pppd/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-sstp.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-sstp-editor.so
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-sstp-pppd-plugin.so
%attr(755,root,root) %{_libexecdir}/nm-sstp-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-sstp-service
%{_prefix}/lib/NetworkManager/VPN/nm-sstp-service.name
%{_datadir}/dbus-1/system.d/nm-sstp-service.conf
%{_datadir}/metainfo/network-manager-sstp.metainfo.xml
