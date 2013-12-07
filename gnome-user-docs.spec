Summary: GNOME User Documentation
Name: gnome-user-docs
Version: 3.6.2
Release: 5
License: GFDL
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
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
%configure2_5x

%make

%install
%makeinstall_std

#find_lang gnome-help

%files 
#FIXME: find-lang can't deal with %{_datadir}/help
#-f gnome-help.lang
%doc README NEWS
%{_datadir}/help/C/*
%lang(cs) %{_datadir}/help/cs/gnome-help
%lang(ca) %{_datadir}/help/ca/gnome-help
%lang(de) %{_datadir}/help/de/gnome-help
%lang(el) %{_datadir}/help/el/gnome-help
%lang(es) %{_datadir}/help/es/gnome-help
%lang(fi) %{_datadir}/help/fi/gnome-help
%lang(fr) %{_datadir}/help/fr/gnome-help
%lang(gl) %{_datadir}/help/gl/gnome-help
%lang(hi) %{_datadir}/help/hi/gnome-help
%lang(hu) %{_datadir}/help/hu/gnome-help
%lang(id) %{_datadir}/help/id/gnome-help
%lang(it) %{_datadir}/help/it/gnome-help
%lang(ja) %{_datadir}/help/ja/gnome-help
%lang(lv) %{_datadir}/help/lv/gnome-help
%lang(nl) %{_datadir}/help/nl/gnome-help
%lang(pa) %{_datadir}/help/pa/gnome-help
%lang(pt_BR) %{_datadir}/help/pt_BR/gnome-help
%lang(ru) %{_datadir}/help/ru/gnome-help
%lang(sl) %{_datadir}/help/sl/gnome-help
%lang(sr) %{_datadir}/help/sr/gnome-help
%lang(sr@latin) %{_datadir}/help/sr@latin/gnome-help
%lang(sv) %{_datadir}/help/sv/gnome-help
%lang(te) %{_datadir}/help/te/gnome-help
%lang(vi) %{_datadir}/help/vi/gnome-help
