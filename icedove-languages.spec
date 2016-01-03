# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=31.4.0
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Icedove
Summary(pl.UTF-8):	Pakiety językowe dla Icedove
Name:		icedove-languages
Version:	38.5.0
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	70fb915f31e9d96557b51e661893a20d
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	997192514f361f4e787a15de01783ab9
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	62ec7e1fdd03d174e455ba9714914013
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	e5dd6b6217947999a5ad1dc4fd760462
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	d79b2b1d4458517e0742900dd2a6058c
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	32e9eced68e021f3416eabb8916986e5
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	21bf014d5c4d689af9e4cb7dc17dcc52
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	631a85b5d454f8c4c553ac259f895951
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	cc6c8cb2d6d6a897411922e01d423a13
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	e36b2673996247c1570c21592b1d2de9
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	cf6d030a87538194f70039f0145c862f
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	79517034cef77103bf48970e18c9b7da
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	c4bdaabdcfdbea73de8dbd1e526f7606
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	974a824746a63ab5679ed4725ca5b6d2
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	bb649b9ed1af1f104ab342aee562110a
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	f895b1c8ceb7a788219e6e6df7cbe398
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	c6baecbdf7f416932c5c108b5bbabfac
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	580f110e7ec107ce67ef5d7ccdb9698e
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	3bb8c389bbd7f1dbc8697d1c591bd9a9
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	ff0437703db0408dba14005e4951b65e
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	3e3b49e40cd2209a64bb56ebf7a6cde0
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	c503c8e1d140d007d32a052c04ed657a
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	8c5d18adc5fb4c24bcd8e88fe9611be2
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	14b5ea99dab49962f9611a9ddec374a6
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	be7ce76e74987c914262115893b68aa8
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	9028ee2f377e153b5ae26b4ff07f41b7
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	c98546e992365e3727102f49bc032831
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	f0e22e274ee9c1f82f367d70440b9a3b
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	c329ac2f367f80ee71ef7c12ff05db3f
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	d3a43f8f5aa5858f9cac69d802884087
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	6e56c014239218019eb97aae29504cbb
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	a3745e118882d0e13f0baa566ebaf0c6
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	7a896f79a235a1ee01221e3bce8e3400
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	33449f66dbf48f3ed9072430e91b2480
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	d5ed4ff13ceb564ff36954b670275f4a
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	d7e113922a500367fad7e5d801a8b256
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	a1d8c30ca1c80a543f3f40d7c72cf2d6
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	6ee9e518918cafb2293e2cee06e196eb
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	e7d427a6e2bb70fc39623090984e2f8e
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	4d7b475afeb7a3a1603d44082ac2538b
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	4dbfb3c01f16234a551a8b0092d192fa
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	8344678b5ab8cb0e90ff859b76f5df7d
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	d38f6ac503e56426d6d716c81fb26692
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	849ddb353c4f5d4eac5475188802eb60
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	4b04df9753b0e0dcc0e2ed1aa94b0735
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	28e0957085b52bee3aa11e46b0f93f0e
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	fd86cc063e6eda802968181048a131cf
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	adcd548d1adae69b42c4a26bf6f80baa
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	d5d30fb05007b4936d0a2b01396bdd59
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	67804f11cf515ba3943c1019daf0e776
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	8d47982cf7e1130055bc1f8139879482
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	e7713e79a7c28d7a03bf418d09341ae4
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	be86e551496c12250f85ed5d0ed051df
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	5f26cb4679bc4ec162e7be84630347b8
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	65b1c36008e6606d519c1e26eacefb55
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
Obsoletes:	mozilla-thunderbird-lang-ar

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
Obsoletes:	mozilla-thunderbird-lang-ast

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
Obsoletes:	mozilla-thunderbird-lang-be

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
Obsoletes:	mozilla-thunderbird-lang-bg

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
Obsoletes:	mozilla-thunderbird-lang-bn

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
Obsoletes:	mozilla-thunderbird-lang-br

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
Obsoletes:	mozilla-thunderbird-lang-ca

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
Obsoletes:	mozilla-thunderbird-lang-cs

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
Obsoletes:	mozilla-thunderbird-lang-da

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
Obsoletes:	mozilla-thunderbird-lang-de

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
Obsoletes:	mozilla-thunderbird-lang-el

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
Obsoletes:	mozilla-thunderbird-lang-en_GB

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
Obsoletes:	mozilla-thunderbird-lang-en_US

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
Obsoletes:	mozilla-thunderbird-lang-es_AR

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
Obsoletes:	mozilla-thunderbird-lang-es

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
Obsoletes:	mozilla-thunderbird-lang-et

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
Obsoletes:	mozilla-thunderbird-lang-eu

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
Obsoletes:	mozilla-thunderbird-lang-fi

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
Obsoletes:	mozilla-thunderbird-lang-fr

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
Obsoletes:	mozilla-thunderbird-lang-fy

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
Obsoletes:	mozilla-thunderbird-lang-ga

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
Obsoletes:	mozilla-thunderbird-lang-gd

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
Obsoletes:	mozilla-thunderbird-lang-gl

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
Obsoletes:	mozilla-thunderbird-lang-he

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
Obsoletes:	mozilla-thunderbird-lang-hu

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
Obsoletes:	mozilla-thunderbird-lang-id

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
Obsoletes:	mozilla-thunderbird-lang-is

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
Obsoletes:	mozilla-thunderbird-lang-it

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
Obsoletes:	mozilla-thunderbird-lang-ja

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
Obsoletes:	mozilla-thunderbird-lang-ko

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
Obsoletes:	mozilla-thunderbird-lang-lt

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
Obsoletes:	mozilla-thunderbird-lang-nb

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
Obsoletes:	mozilla-thunderbird-lang-nl

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
Obsoletes:	mozilla-thunderbird-lang-nn

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
Obsoletes:	mozilla-thunderbird-lang-pa

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
Obsoletes:	mozilla-thunderbird-lang-pt_BR

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
Obsoletes:	mozilla-thunderbird-lang-pt

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
Obsoletes:	mozilla-thunderbird-lang-rm

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
Obsoletes:	mozilla-thunderbird-lang-ro

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
Obsoletes:	mozilla-thunderbird-lang-ru

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
Obsoletes:	mozilla-thunderbird-lang-si

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
Obsoletes:	mozilla-thunderbird-lang-sk

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
Obsoletes:	mozilla-thunderbird-lang-sl

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
Obsoletes:	mozilla-thunderbird-lang-sq

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
Obsoletes:	mozilla-thunderbird-lang-sr

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
Obsoletes:	mozilla-thunderbird-lang-sv

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
Obsoletes:	mozilla-thunderbird-lang-ta_LK

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
Obsoletes:	mozilla-thunderbird-lang-tr

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
Obsoletes:	mozilla-thunderbird-lang-uk

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
Obsoletes:	mozilla-thunderbird-lang-vi

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
Obsoletes:	mozilla-thunderbird-lang-zh_CN

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
Obsoletes:	mozilla-thunderbird-lang-zh_TW

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
	# rebrand locale for Icedove
	cd $lang
	cp -p $file .
	unzip -q $lang.xpi install.rdf $fix1
	sed -i -e 's/Mozilla Thunderbird/Icedove/g; s/Thunderbird/Icedove/g;' $fix1
	zip -q0 $lang.xpi $fix1
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
