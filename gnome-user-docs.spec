%define _disable_rebuild_configure 1
Summary: GNOME User Documentation
Name: gnome-user-docs
Version:  3.30.1
Release: 1
License: GFDL
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.14/%{name}-%{version}.tar.xz
Group: Books/Other
Url: http://www.gnome.org/
BuildArch: noarch

BuildRequires: itstool
BuildRequires: xsltproc
BuildRequires: pkgconfig(gnome-doc-utils)

%description
This package contains the GNOME Glossary, Introduction to GNOME, and a Unix
Primer.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%find_lang gnome-help --with-gnome --all-name

%files -f gnome-help.lang
%doc README NEWS


