#
# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
#
Summary:	Polish resources for Icedove
Summary(pl.UTF-8):	Polskie pliki językowe dla Icedove
Name:		icedove-lang-pl
Version:	3.0.1
Release:	1
License:	GPL
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	24fb5db23baf9461ec01774e136ae8e3
URL:		http://www.thunderbird.pl/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_icedovedir	%{_datadir}/icedove
%define		_chromedir	%{_icedovedir}/chrome

%description
Polish resources for Icedove.

%description -l pl.UTF-8
Polskie pliki językowe dla Icedove.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_icedovedir}/{defaults/profile,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/pl.jar $RPM_BUILD_ROOT%{_chromedir}/pl-PL.jar
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_icedovedir}/defaults/profile
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
cat $RPM_BUILD_ROOT%{_libdir}/chrome.manifest | sed 's: pl : pl-PL :g; s:chrome/pl:pl-PL:g ' \
	> $RPM_BUILD_ROOT%{_chromedir}/pl-PL.manifest
# rebrand locale for iceweasel
cd $RPM_BUILD_ROOT%{_chromedir}
unzip pl-PL.jar locale/pl/branding/brand.dtd locale/pl/branding/brand.properties \
	locale/pl/messenger/aboutDialog.dtd locale/pl/messenger/start.dtd \
	locale/pl/messenger-newsblog/newsblog.properties
sed -i -e 's/Mozilla Thunderbird/Icedove/g; s/Thunderbird/Icedove/g;' \
	locale/pl/branding/brand.dtd locale/pl/branding/brand.properties
sed -i -e 's/Thunderbird/Icedove/g;' locale/pl/messenger/start.dtd \
	locale/pl/messenger-newsblog/newsblog.properties
grep -e '\<ENTITY' locale/pl/messenger/aboutDialog.dtd \
	> locale/pl/messenger/aboutDialog.dtd.new
sed -i -e '/copyrightText/s/^\(.*\)\..*Thunderbird.*/\1\./g; s/\r//g; /copyrightText/s/$/" >/g;' \
	locale/pl/messenger/aboutDialog.dtd.new
mv -f locale/pl/messenger/aboutDialog.dtd.new locale/pl/messenger/aboutDialog.dtd
zip -0 pl-PL.jar locale/pl/branding/brand.dtd locale/pl/branding/brand.properties \
	locale/pl/messenger/aboutDialog.dtd locale/pl/messenger/start.dtd \
	locale/pl/messenger-newsblog/newsblog.properties
rm -f locale/pl/branding/brand.dtd locale/pl/branding/brand.properties \
	locale/pl/messenger/aboutDialog.dtd locale/pl/messenger/start.dtd \
	locale/pl/messenger-newsblog/newsblog.properties

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << 'EOF'
NOTE: You must also change your default useragent locale:
  Open Icedove and go to Edit>Preferences>Advenced>General>Config Editor then
  find "general.useragent.locale" and change value
  to "pl-PL" then restart Icedove.

EOF

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-PL.manifest
#%{_chromedir}/chromelist.txt
%{_icedovedir}/defaults/profile/*.rdf
