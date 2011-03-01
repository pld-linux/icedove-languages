# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
Summary:	Language packs for Icedove
Name:		icedove-languages
Version:	3.1.8
Release:	1
License:	GPL
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	194b30bd8ba8109c2a7a7be767ca14f3
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source1-md5:	a5e841aa80030fd005d65476ccb4620d
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

%package -n icedove-lang-et
Summary:	Estonian resources for Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-et
Estonian resources for Icedove.

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

	%{__sed} -i -e 's/Mozilla Thunderbird/Icedove/g; s/Thunderbird/Icedove/g;' \
		locale/$lang/branding/brand.dtd locale/$lang/branding/brand.properties
	%{__sed} -i -e 's/Thunderbird/Icedove/g;' locale/$lang/messenger-newsblog/newsblog.properties

	grep -e '\<ENTITY' locale/$lang/messenger/aboutDialog.dtd \
		> locale/$lang/messenger/aboutDialog.dtd.new
	%{__sed} -i -e '/copyrightText/s/^\(.*\)\..*Thunderbird.*/\1\./g; s/\r//g; /copyrightText/s/$/" >/g;' \
		locale/$lang/messenger/aboutDialog.dtd.new
	mv -f locale/$lang/messenger/aboutDialog.dtd.new locale/$lang/messenger/aboutDialog.dtd

	zip -q0 $locale.jar locale/$lang/branding/brand.dtd locale/$lang/branding/brand.properties \
		locale/$lang/messenger/aboutDialog.dtd \
		locale/$lang/messenger-newsblog/newsblog.properties

	%{__rm} -r locale
	cd ../..
}
%define __unzip unpack
# LANGUAGE LOCALE
cat <<'EOF' > locales.txt
et et-EE
pl pl-PL
EOF
%setup -qcT -a0 -a1

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

# NOTE:
# I wish i could use banner macro here, but it does not work with nesting well
%define post_banner() \
cat >&2 <<EOF\
NOTE:\
  To change your default useragent locale: \
  Open Icedove and go to Edit>Preferences>Advenced>General>Config Editor then \
  find "general.useragent.locale" and change value \
  to "%2" then restart Icedove. \
\
  Or install "Quick Locale Switcher" extension \
\
EOF\
%{nil}

%{nil}
%post -n icedove-lang-et
%post_banner et et-EE

%post -n icedove-lang-pl
%post_banner pl pl-PL

%files -n icedove-lang-et
%defattr(644,root,root,755)
%{chromedir}/et-EE.jar
%{chromedir}/et-EE.manifest

%files -n icedove-lang-pl
%defattr(644,root,root,755)
%{chromedir}/pl-PL.jar
%{chromedir}/pl-PL.manifest
#%{chromedir}/chromelist.txt
%{icedovedir}/defaults/profile/*.rdf
