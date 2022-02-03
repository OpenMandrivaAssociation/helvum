%define _empty_manifest_terminate_build 0
Name:           helvum
Version:        0.3.4
Release:        1
Group:          Sound/Utilities
Summary:        A GTK patchbay for PipeWire
License:        GPL3.0
URL:            https://gitlab.freedesktop.org/pipewire/helvum
Source:         https://gitlab.freedesktop.org/pipewire/helvum/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: appstream-util
BuildRequires: cargo
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libpipewire-0.3)
  
Requires: gtk4.0
Requires: pipewire

%description
Helvum is a GTK-based, writen in Rust patchbay for PipeWire, inspired by the JACK tool Catia.

%prep
%autosetup -p1

%build
# Possible also to call directly cargo build/install without meson.
%meson --buildtype=release
%meson_build

%install
%meson_install

%files
%{_bindir}/helvum
%{_datadir}/applications/org.pipewire.Helvum.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.pipewire.Helvum.metainfo.xml
