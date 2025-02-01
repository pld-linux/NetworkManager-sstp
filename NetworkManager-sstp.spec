#
# Conditional build:
%bcond_without	gtk4	# Gtk4 version of editor plugin (GNOME 42+)

Summary:	NetworkManager VPN integration for SSTP
Summary(pl.UTF-8):	Integracja NetworkManagera z protokołem SSTP
Name:		NetworkManager-sstp
Version:	1.3.2
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-sstp/1.3/%{name}-%{version}.tar.xz
# Source0-md5:	52acb4a46dd96b7864419410fae8d76e
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.7.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.8.0
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.20
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	gnutls-devel >= 2.12
BuildRequires:	gtk+3-devel >= 3.4
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
%{?with_gtk4:BuildRequires:	libnma-gtk4-devel >= 1.8.33}
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:2.5.0
BuildRequires:	sstp-client-devel >= 1.0.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.7.0
Requires:	NetworkManager-gtk-lib >= 1.8.0
Requires:	glib2 >= 1:2.40
Requires:	gtk+3 >= 3.4
%{?with_gtk4:Requires:	libnma-gtk4 >= 1.8.33}
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{?with_gtk4:--with-gtk4} \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins
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
%if %{with gtk4}
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-sstp-editor.so
%endif
%attr(755,root,root) %{_libdir}/pppd/plugins/nm-sstp-pppd-plugin.so
%attr(755,root,root) %{_libexecdir}/nm-sstp-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-sstp-service
%{_prefix}/lib/NetworkManager/VPN/nm-sstp-service.name
%{_datadir}/dbus-1/system.d/nm-sstp-service.conf
%{_datadir}/metainfo/network-manager-sstp.metainfo.xml
