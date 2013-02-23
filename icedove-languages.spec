# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=10.0.2
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Icedove
Summary(pl.UTF-8):	Pakiety językowe dla Icedove
Name:		icedove-languages
Version:	17.0.3
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	190c2a2d0f6e37f34aad8e1d6a03e338
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	5903f4f5f58872c4d0608fbb7c807535
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	13c85cc3806b98eaa864413287e9801e
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	87e87b687423e62f296cbefc78bfe6b7
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	5ab26b0a9ec10203d5fbeb4e6d8c37fe
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	b9aada85e32037355eaf72d6a333fdb6
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	d62b10c899df633f01361c8fea86a2d5
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	9b3ee7f3abc87787165678d4f90414eb
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	3326fa522ecd85eb2726cd759396cf7b
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	62fc373ca8e4c97008b9d570e767e3c1
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	ca0eac94b397dce125867c68129d892c
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	23c99a2476db4dba10e30bf91923a071
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	455a5bd79bc3c39c699cf28648336757
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	eb50edbab0549ffcbe0bbe4bd4034ad6
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	b939558426b00bb71d22eea9cca7934b
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	df6865ea5301f822e935de490c283f70
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	c9d36ce960073d54000566eae29d1a64
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	c616e7eaf40247f46962bfaed25f0467
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	bd6f55ba2ba60def8cfef38361fd453a
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	9f2057d1d5ec2e2b24fbf7896a070f66
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	520ef14dac72b2ebf4865fd42fc84d3c
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	855b8de7ae0a924fb1e14f746ee62d20
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	53cc664506d559721a1fca0641f6c6a9
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	5c7970773b74c02c27aa36158f9d3e9f
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	3f0992dfe456ac5752811cef77715e71
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	5f2566a8d6b620a3aa9aa1cf03342f6a
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	a68fcee2081e2f48ffe901a4621b282f
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	a5f4f72cabc4e4d4e85666f5b6a6c782
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	fbab0783479643d8f3dd664eb2080169
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	f50a7c6f661b4171bab2a1161722813e
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	95f93d9147e665854cebb9268517d2c4
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	2202b08bf6321eea60845c29d9901d9e
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	f26fc62be83107e03fe6a1304307d6ce
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	d152f01e8eff70128748b7eb5a4a165c
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	b1dec10579653e2675107b9eabe9d511
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	4fe020d43cde68db9225600f6f415d0f
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	fffd7ed634342ea46dc09c360418ac98
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	fe3e5a47746afb712a57f32598dbbaa4
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	ba0f8f8f43302efda57a156088d6c0d0
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	7d9a8131093c300c557bd0a73fdcc4b7
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	5557ebdcd2583ba77ee994a199850292
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	64ef30075e847f2167615c99af3a4d81
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	3b7d480e1d92b63d45d56d8bf997166b
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	9b691b1aa18b3c364cb445bf1672f7bc
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	080576b0e1665da96610b7aa9ec8a0b3
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	d1405f684573fcc9c452cf938bbe239f
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	e98489bdc57c482dfc18b59a70c4e379
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	3eb66537793360afd3b3a7afb07db129
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	4f546164884e4381572bb1f3f6e7d1f6
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	f247dbf3c9817de173d7be5471d10553
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	a72957a7e5a82aa8fffff126e8516971
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	6365259d4134b06d1d7af1bfe876c384
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	98e4c7fe88d6d333884f8b1f41c5bb26
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	758836dee42f0503769c58396170eed5
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	36619bd5a5adbaac5f02fe0d5596e52a
URL:		http://www.pld-linux.org/Packages/Icedove
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		icedovedir		%{_libdir}/icedove

%description
Language packs for Icedove.

%description -l pl.UTF-8
Pakiety językowe dla Icedove.

%package -n icedove-lang-ar
Summary:	Arabic resources for Icedove
Summary(pl.UTF-8):	Arabskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ar
Arabic resources for Icedove.

%description -n icedove-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Icedove.

%package -n icedove-lang-ast
Summary:	Asturian resources for Icedove
Summary(pl.UTF-8):	Asturskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ast
Asturian resources for Icedove.

%description -n icedove-lang-ast -l pl.UTF-8
Asturskie pliki językowe dla Icedove.

%package -n icedove-lang-be
Summary:	Belarusian resources for Icedove
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-be
Belarusian resources for Icedove.

%description -n icedove-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Icedove.

%package -n icedove-lang-bg
Summary:	Bulgarian resources for Icedove
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-bg
Bulgarian resources for Icedove.

%description -n icedove-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Icedove.

%package -n icedove-lang-bn
Summary:	Bengali (Bangladesh) resources for Icedove
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Icedove (wersja dla Bangladeszu)
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-bn
Bengali (Bangladesh) resources for Icedove.

%description -n icedove-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Icedove (wersja dla Bangladeszu).

%package -n icedove-lang-br
Summary:	Breton resources for Icedove
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-br
Breton resources for Icedove.

%description -n icedove-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Icedove.

%package -n icedove-lang-ca
Summary:	Catalan resources for Icedove
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ca
Catalan resources for Icedove.

%description -n icedove-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Icedove.

%package -n icedove-lang-cs
Summary:	Czech resources for Icedove
Summary(pl.UTF-8):	Czeskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-cs
Czech resources for Icedove.

%description -n icedove-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Icedove.

%package -n icedove-lang-da
Summary:	Danish resources for Icedove
Summary(pl.UTF-8):	Duńskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-da
Danish resources for Icedove.

%description -n icedove-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Icedove.

%package -n icedove-lang-de
Summary:	German resources for Icedove
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-de
German resources for Icedove.

%description -n icedove-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Icedove.

%package -n icedove-lang-el
Summary:	Greek resources for Icedove
Summary(pl.UTF-8):	Greckie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-el
Greek resources for Icedove.

%description -n icedove-lang-el -l pl.UTF-8
Greckie pliki językowe dla Icedove.

%package -n icedove-lang-en_GB
Summary:	English (British) resources for Icedove
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-en_GB
English (British) resources for Icedove.

%description -n icedove-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Icedove.

%package -n icedove-lang-en_US
Summary:	English (American) resources for Icedove
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-en_US
English (American) resources for Icedove.

%description -n icedove-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Icedove.

%package -n icedove-lang-es_AR
Summary:	Spanish (Andorra) resources for Icedove
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Icedove (wersja dla Andory)
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-es_AR
Spanish (Andorra) resources for Icedove.

%description -n icedove-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Icedove (wersja dla Andory).

%package -n icedove-lang-es
Summary:	Spanish (Spain) resources for Icedove
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Icedove (wersja dla Hiszpanii)
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-es
Spanish (Spain) resources for Icedove.

%description -n icedove-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Icedove (wersja dla Hiszpanii).

%package -n icedove-lang-et
Summary:	Estonian resources for Icedove
Summary(pl.UTF-8):	Estońskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-et
Estonian resources for Icedove.

%description -n icedove-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Icedove.

%package -n icedove-lang-eu
Summary:	Basque resources for Icedove
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-eu
Basque resources for Icedove.

%description -n icedove-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Icedove.

%package -n icedove-lang-fi
Summary:	Finnish resources for Icedove
Summary(pl.UTF-8):	Fińskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-fi
Finnish resources for Icedove.

%description -n icedove-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Icedove.

%package -n icedove-lang-fr
Summary:	French resources for Icedove
Summary(pl.UTF-8):	Francuskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-fr
French resources for Icedove.

%description -n icedove-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Icedove.

%package -n icedove-lang-fy
Summary:	Frisian resources for Icedove
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-fy
Frisian resources for Icedove.

%description -n icedove-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Icedove.

%package -n icedove-lang-ga
Summary:	Irish resources for Icedove
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ga
Irish resources for Icedove.

%description -n icedove-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Icedove.

%package -n icedove-lang-gd
Summary:	Gaelic resources for Icedove
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-gd
Gaelic resources for Icedove.

%description -n icedove-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Icedove.

%package -n icedove-lang-gl
Summary:	Galician resources for Icedove
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-gl
Galician resources for Icedove.

%description -n icedove-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Icedove.

%package -n icedove-lang-he
Summary:	Hebrew resources for Icedove
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-he
Hebrew resources for Icedove.

%description -n icedove-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Icedove.

%package -n icedove-lang-hr
Summary:	Croatian resources for Icedove
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-hr

%description -n icedove-lang-hr
Croatian resources for Icedove.

%description -n icedove-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Icedove.

%package -n icedove-lang-hu
Summary:	Hungarian resources for Icedove
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-hu
Hungarian resources for Icedove.

%description -n icedove-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Icedove.

%package -n icedove-lang-hy
Summary:	Armenian resources for Icedove
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-hy

%description -n icedove-lang-hy
Armenian resources for Icedove.

%description -n icedove-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Icedove.

%package -n icedove-lang-id
Summary:	Indonesian resources for Icedove
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-id
Indonesian resources for Icedove.

%description -n icedove-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Icedove.

%package -n icedove-lang-is
Summary:	Icelandic resources for Icedove
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-is
Icelandic resources for Icedove.

%description -n icedove-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Icedove.

%package -n icedove-lang-it
Summary:	Italian resources for Icedove
Summary(pl.UTF-8):	Włoskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-it
Italian resources for Icedove.

%description -n icedove-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Icedove.

%package -n icedove-lang-ja
Summary:	Japanese resources for Icedove
Summary(pl.UTF-8):	Japońskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ja
Japanese resources for Icedove.

%description -n icedove-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Icedove.

%package -n icedove-lang-ko
Summary:	Korean resources for Icedove
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ko
Korean resources for Icedove.

%description -n icedove-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Icedove.

%package -n icedove-lang-lt
Summary:	Lithuanian resources for Icedove
Summary(pl.UTF-8):	Litewskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-lt
Lithuanian resources for Icedove.

%description -n icedove-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Icedove.

%package -n icedove-lang-nb
Summary:	Norwegian Bokmaal resources for Icedove
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-nb
Norwegian Bokmaal resources for Icedove.

%description -n icedove-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Icedove.

%package -n icedove-lang-nl
Summary:	Dutch resources for Icedove
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-nl
Dutch resources for Icedove.

%description -n icedove-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Icedove.

%package -n icedove-lang-nn
Summary:	Norwegian Nynorsk resources for Icedove
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-nn
Norwegian Nynorsk resources for Icedove.

%description -n icedove-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Icedove.

%package -n icedove-lang-pa
Summary:	Panjabi resources for Icedove
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-pa
Panjabi resources for Icedove.

%description -n icedove-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Icedove.

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

%package -n icedove-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Icedove
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-pt_BR
Portuguese (Brazil) resources for Icedove.

%description -n icedove-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Icedove.

%package -n icedove-lang-pt
Summary:	Portuguese (Portugal) resources for Icedove
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Icedove (wersja dla Portugalii)
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-pt
Portuguese (Portugal) resources for Icedove.

%description -n icedove-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Icedove (wersja dla Portugalii).

%package -n icedove-lang-rm
Summary:	Romansh resources for Icedove
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-rm
Romansh resources for Icedove.

%description -n icedove-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Icedove.

%package -n icedove-lang-ro
Summary:	Romanian resources for Icedove
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ro
Romanian resources for Icedove.

%description -n icedove-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Icedove.

%package -n icedove-lang-ru
Summary:	Russian resources for Icedove
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ru
Russian resources for Icedove.

%description -n icedove-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Icedove.

%package -n icedove-lang-si
Summary:	Sinhala resources for Icedove
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-si
Sinhala resources for Icedove.

%description -n icedove-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Icedove.

%package -n icedove-lang-sk
Summary:	Slovak resources for Icedove
Summary(pl.UTF-8):	Słowackie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-sk
Slovak resources for Icedove.

%description -n icedove-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Icedove.

%package -n icedove-lang-sl
Summary:	Slovene resources for Icedove
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-sl
Slovene resources for Icedove.

%description -n icedove-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Icedove.

%package -n icedove-lang-sq
Summary:	Albanian resources for Icedove
Summary(pl.UTF-8):	Albańskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-sq
Albanian resources for Icedove.

%description -n icedove-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Icedove.

%package -n icedove-lang-sr
Summary:	Serbian resources for Icedove
Summary(pl.UTF-8):	Serbskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-sr
Serbian resources for Icedove.

%description -n icedove-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Icedove.

%package -n icedove-lang-sv
Summary:	Swedish resources for Icedove
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-sv
Swedish resources for Icedove.

%description -n icedove-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Icedove.

%package -n icedove-lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Icedove
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Icedove (wersja dla Sri Lanki)
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-ta_LK
Tamil (Sri Lanka) resources for Icedove.

%description -n icedove-lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Icedove (wersja dla Sri Lanki).

%package -n icedove-lang-tr
Summary:	Turkish resources for Icedove
Summary(pl.UTF-8):	Tureckie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-tr
Turkish resources for Icedove.

%description -n icedove-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Icedove.

%package -n icedove-lang-uk
Summary:	Ukrainian resources for Icedove
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-uk
Ukrainian resources for Icedove.

%description -n icedove-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Icedove.

%package -n icedove-lang-vi
Summary:	Vietnamese resources for Icedove
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-vi
Vietnamese resources for Icedove.

%description -n icedove-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Icedove.

%package -n icedove-lang-zh_CN
Summary:	Simplified Chinese resources for Icedove
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-zh_CN
Simplified Chinese resources for Icedove.

%description -n icedove-lang-zh_CN -l pl.UTF-8
Chińskie (uproszczone) pliki językowe dla Icedove.

%package -n icedove-lang-zh_TW
Summary:	Traditional Chinese resources for Icedove
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Icedove
Group:		I18n
Requires:	icedove >= %{version}
Provides:	icedove-lang-resources = %{version}

%description -n icedove-lang-zh_TW
Traditional Chinese resources for Icedove.

%description -n icedove-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Icedove.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang

	fix1=chrome/$lang/locale/$lang/branding/brand.{dtd,properties}
        fix2=chrome/$lang/locale/$lang/feedback/main.{dtd,properties}
	# rebrand locale for Icedove
	cd $lang
	cp -p $file .
	unzip -q $lang.xpi install.rdf $fix1 $fix2
	sed -i -e 's/Mozilla Thunderbird/Icedove/g; s/Thunderbird/Icedove/g;' $fix1
	sed -i -e 's/Thunderbird/Icedove/g;' $fix2
	zip -q0 $lang.xpi $fix1 $fix2
	if ! grep -q "<em:minVersion>%{version}</em:minVersion>" install.rdf; then
		echo "$lang.xpi most likely doesn't work with icedove %{version}!" >&2
		exit 1
	fi
	%{__rm} -rf chrome install.rdf
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 54 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{icedovedir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{icedovedir}/extensions/langpack-$basename@thunderbird.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icedove-lang-ar
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ar@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ast
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ast@thunderbird.mozilla.org.xpi

%files -n icedove-lang-be
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-be@thunderbird.mozilla.org.xpi

%files -n icedove-lang-bg
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-bg@thunderbird.mozilla.org.xpi

%files -n icedove-lang-bn
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-bn-BD@thunderbird.mozilla.org.xpi

%files -n icedove-lang-br
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-br@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ca
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ca@thunderbird.mozilla.org.xpi

%files -n icedove-lang-cs
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-cs@thunderbird.mozilla.org.xpi

%files -n icedove-lang-da
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-da@thunderbird.mozilla.org.xpi

%files -n icedove-lang-de
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-de@thunderbird.mozilla.org.xpi

%files -n icedove-lang-el
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-el@thunderbird.mozilla.org.xpi

%files -n icedove-lang-en_GB
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-en-GB@thunderbird.mozilla.org.xpi

%files -n icedove-lang-en_US
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-en-US@thunderbird.mozilla.org.xpi

%files -n icedove-lang-es_AR
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-es-AR@thunderbird.mozilla.org.xpi

%files -n icedove-lang-es
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-es-ES@thunderbird.mozilla.org.xpi

%files -n icedove-lang-et
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-et@thunderbird.mozilla.org.xpi

%files -n icedove-lang-eu
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-eu@thunderbird.mozilla.org.xpi

%files -n icedove-lang-fi
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-fi@thunderbird.mozilla.org.xpi

%files -n icedove-lang-fr
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-fr@thunderbird.mozilla.org.xpi

%files -n icedove-lang-fy
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-fy-NL@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ga
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ga-IE@thunderbird.mozilla.org.xpi

%files -n icedove-lang-gd
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-gd@thunderbird.mozilla.org.xpi

%files -n icedove-lang-gl
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-gl@thunderbird.mozilla.org.xpi

%files -n icedove-lang-he
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-he@thunderbird.mozilla.org.xpi

%files -n icedove-lang-hr
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-hr@thunderbird.mozilla.org.xpi

%files -n icedove-lang-hu
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-hu@thunderbird.mozilla.org.xpi

%files -n icedove-lang-hy
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-hy-AM@thunderbird.mozilla.org.xpi

%files -n icedove-lang-id
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-id@thunderbird.mozilla.org.xpi

%files -n icedove-lang-is
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-is@thunderbird.mozilla.org.xpi

%files -n icedove-lang-it
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-it@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ja
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ja@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ko
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ko@thunderbird.mozilla.org.xpi

%files -n icedove-lang-lt
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-lt@thunderbird.mozilla.org.xpi

%files -n icedove-lang-nb
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-nb-NO@thunderbird.mozilla.org.xpi

%files -n icedove-lang-nl
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-nl@thunderbird.mozilla.org.xpi

%files -n icedove-lang-nn
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-nn-NO@thunderbird.mozilla.org.xpi

%files -n icedove-lang-pa
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-pa-IN@thunderbird.mozilla.org.xpi

%files -n icedove-lang-pl
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-pl@thunderbird.mozilla.org.xpi

%files -n icedove-lang-pt_BR
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-pt-BR@thunderbird.mozilla.org.xpi

%files -n icedove-lang-pt
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-pt-PT@thunderbird.mozilla.org.xpi

%files -n icedove-lang-rm
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-rm@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ro
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ro@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ru
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ru@thunderbird.mozilla.org.xpi

%files -n icedove-lang-si
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-si@thunderbird.mozilla.org.xpi

%files -n icedove-lang-sk
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-sk@thunderbird.mozilla.org.xpi

%files -n icedove-lang-sl
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-sl@thunderbird.mozilla.org.xpi

%files -n icedove-lang-sq
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-sq@thunderbird.mozilla.org.xpi

%files -n icedove-lang-sr
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-sr@thunderbird.mozilla.org.xpi

%files -n icedove-lang-sv
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-sv-SE@thunderbird.mozilla.org.xpi

%files -n icedove-lang-ta_LK
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-ta-LK@thunderbird.mozilla.org.xpi

%files -n icedove-lang-tr
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-tr@thunderbird.mozilla.org.xpi

%files -n icedove-lang-uk
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-uk@thunderbird.mozilla.org.xpi

%files -n icedove-lang-vi
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-vi@thunderbird.mozilla.org.xpi

%files -n icedove-lang-zh_CN
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-zh-CN@thunderbird.mozilla.org.xpi

%files -n icedove-lang-zh_TW
%defattr(644,root,root,755)
%{icedovedir}/extensions/langpack-zh-TW@thunderbird.mozilla.org.xpi
