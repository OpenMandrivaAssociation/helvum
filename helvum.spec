Name:           helvum
Version:        0.3.4
Release:        1
Group:          Sound/Utilities
Summary:        A GTK patchbay for PipeWire
License:        GPL3.0
URL:            https://gitlab.freedesktop.org/pipewire/helvum
Source:         https://gitlab.freedesktop.org/pipewire/helvum/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: cargo
BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libpipewire-0.3)
  
Requires: gtk4.0

%description
Helvum is a GTK-based, writen in Rust patchbay for PipeWire, inspired by the JACK tool Catia.

%prep
%autosetup -p1

%build
# Possible also to call directly cargo build/install without meson.
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/helvum
%{_datadir}/applications/org.pipewire.Helvum.desktop
%{_datadir}/icons/hicolor/
