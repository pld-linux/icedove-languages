# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
Summary:	Language packs for Icedove
Name:		icedove-languages
Version:	3.1.5
Release:	1
License:	GPL
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	19246d3b9d3a40d61be3be510ddda5f4
URL:		http://www.pld-linux.org/Packages/Icedove
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		icedovedir		%{_datadir}/icedove
%define		chromedir		%{icedovedir}/chrome

%description
Language packs for Icedove.

%package -n icedove-lang-pl
Summary:	Polish resources for Icedove
Summary(pl.UTF-8):	Polskie pliki językowe dla Icedove
Group:		I18n
URL:		http://www.thunderbird.pl/
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pl

%description -n icedove-lang-pl
Polish resources for Icedove.

%description -n icedove-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Icedove.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	%{__unzip} $args -d $lang $file

	locale=$(awk -vl=$lang '$1 == l{print $2}' %{_builddir}/locales.txt)
	cd $lang
	install -d defaults/profile
	sed -i -e "s@chrome/$lang@$locale@" chrome.manifest
	[ $lang = $locale ] || mv chrome/$lang.jar chrome/$locale.jar
	mv chrome.manifest chrome/$locale.manifest
	mv install.rdf defaults/profile

	# rebrand locale for Icedove
	cd chrome
	%{__unzip} -q $locale.jar locale/$lang/branding/brand.dtd locale/$lang/branding/brand.properties \
		locale/$lang/messenger/aboutDialog.dtd \
		locale/$lang/messenger-newsblog/newsblog.properties

	sed -i -e 's/Mozilla Thunderbird/Icedove/g; s/Thunderbird/Icedove/g;' \
		locale/$lang/branding/brand.dtd locale/$lang/branding/brand.properties
	sed -i -e 's/Thunderbird/Icedove/g;' locale/$lang/messenger-newsblog/newsblog.properties

	grep -e '\<ENTITY' locale/$lang/messenger/aboutDialog.dtd \
		> locale/$lang/messenger/aboutDialog.dtd.new
	sed -i -e '/copyrightText/s/^\(.*\)\..*Thunderbird.*/\1\./g; s/\r//g; /copyrightText/s/$/" >/g;' \
		locale/$lang/messenger/aboutDialog.dtd.new
	mv -f locale/$lang/messenger/aboutDialog.dtd.new locale/$lang/messenger/aboutDialog.dtd

	zip -q0 $locale.jar locale/$lang/branding/brand.dtd locale/$lang/branding/brand.properties \
		locale/$lang/messenger/aboutDialog.dtd \
		locale/$lang/messenger-newsblog/newsblog.properties

	rm -rf locale
	cd ../..
}
%define __unzip unpack
# LANGUAGE LOCALE
cat <<'EOF' > locales.txt
pl pl-PL
EOF
%setup -qcT -a 0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{chromedir},%{icedovedir}/defaults/profile}
for a in */chrome; do
	cp -a $a/* $RPM_BUILD_ROOT%{chromedir}
done

# FIXME one language to dominate
cp -a pl/defaults/profile/*.rdf $RPM_BUILD_ROOT%{icedovedir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%post -n icedove-lang-pl
cat << 'EOF'
NOTE: You must also change your default useragent locale:
  Open Icedove and go to Edit>Preferences>Advenced>General>Config Editor then
  find "general.useragent.locale" and change value
  to "pl-PL" then restart Icedove.

EOF

%files -n icedove-lang-pl
%defattr(644,root,root,755)
%{chromedir}/pl-PL.jar
%{chromedir}/pl-PL.manifest
#%{chromedir}/chromelist.txt
%{icedovedir}/defaults/profile/*.rdf
