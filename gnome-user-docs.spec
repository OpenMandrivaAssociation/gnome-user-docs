%define _disable_rebuild_configure 1
Summary: GNOME User Documentation
Name: gnome-user-docs
Version: 51.0
Release: 1
License: GFDL
Source0: https://ftp.gnome.org/pub/GNOME/sources/%{name}/48/%{name}-%{version}.tar.xz
Group: Books/Other
Url: https://www.gnome.org/
BuildArch: noarch

BuildRequires: meson
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: xsltproc
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: yelp-tools

%description
This package contains the GNOME Glossary, Introduction to GNOME, and a Unix
Primer.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang gnome-help --with-gnome --all-name

%files -f gnome-help.lang
%doc README* NEWS
