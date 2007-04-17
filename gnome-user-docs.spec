Summary: GNOME User Documentation
Name: gnome-user-docs
Version: 2.18.1
Release: %mkrel 1
License: FDL
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Group: Books/Other
Url: http://www.gnome.org/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: scrollkeeper pkgconfig
BuildRequires: gnome-doc-utils >= 0.5.6 libxslt-proc
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3
Obsoletes: gnome-users-guide
Provides: gnome-users-guide

%description
This package contains the GNOME Glossary, Introduction to GNOME, and a Unix
Primer.

%prep
%setup -q

%build
%configure2_5x
# parallel compilation is broken
make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name
rm -rf %buildroot/var/lib/scrollkeeper
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%clean 
rm -rf $RPM_BUILD_ROOT

%post
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi

%postun
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi

%files -f %{name}.lang
%defattr(-, root, root)
%doc README NEWS
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
