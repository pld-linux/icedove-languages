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
Version:	17.0.2
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	46afc83b0330e886e13a90668d3ce24b
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	e60a58f5d2db4c2250443050d9bc0723
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	fdf3af74b22b4198cb0ecad6024d2b14
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	0805550896db8e15a8fa489070788f48
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	f83c1404b0553ea3f44189344714f6cc
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	e502badb7fcc91b312c5eeb17cc722fd
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	8b88a0ba24bfde3da1c8652fe75dc8cd
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	bd82faab59437b0f33dccead7efc7eb8
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	da57be7a409b5b8d406132f25db43f7a
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	bf949e10311d05dc7c373dc915bdaa48
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	539dfc1c23df958ecc6654c4d2170f6d
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	9954e584899174c0f948f064d9c2b757
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	ff91eebb4f906a1d171493d7ac186cd6
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	c1e44b36e9e8e72c7e336787d17781ba
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	c7213e8e055296c2c175673b1976fffa
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	c917790fb8e15e3cfbb560b437a3372e
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	8b110f770bf16b3fd6c32d8297fe060f
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	74af1c253e47fc8199f72b3fde055e7e
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	0a4b2ab366ef3dcd22ad51d22260199d
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	275054e5e293e6bb518e17629b0ca751
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	142a36b1f148df04384ecd379368c514
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	bf8369a767b1c9c1fb6dca0d978c67fe
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	f3f187b2a37372ccbd4dec7d6016f35d
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	a78d3e09c33cc08928fe2255fbd996d1
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	b18a056da828bc758540b493608a0c66
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	d7cea5baebc89330fcbecaba9cc0c876
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	7c761f8dff55f1d4bfe216b461f42e4b
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	52a675528c8506eb8a21effd40c3b440
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	fe48d12b0d8b4e5bfb3d5adb7bfcc4a5
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	d519210f939cc5bd339a8387a5af4f23
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	cfc3a7ca61f7f0703580d7a0393ef50c
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	3714b92309d6e6b31963c342ab5b75de
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	5cdfbe9c435c45712319e548e813564e
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	3c66e0e2e0d5695a5c6c28281f77725a
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	221b952f4209662fa8b05530edadb982
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	93aadbe17b55931210b34407d8c04b46
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	5ccfea7c46a94a5988bce3033f073c0c
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	f65e9b5a3ccf7031c91e80a2c8536319
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	15f4b7a17cc2dfd8d87467f7977b8e32
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	e44115576042e8ab9eabb48db8bab7a4
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	cead812402e95a1449e722a35448992b
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	03b45e2eb5764070b930392013750aad
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	6f043ec05521ef93fbbf3aaf7b623635
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	5a4f890227addd059cc7accc4e0459c9
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	43c778dcc6e108355875ac61ae93c155
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	dcb7efd90f52aa606f62e9dde685eb8d
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	ecbbf57a1b799181552daf0f3bf00c15
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	6702d779aba24ea3a8ce33cf02992f68
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	7baf493bc25d3f53bc8c1492675f3d34
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	99dabbea411ea1d0f7c79c7b07892fd0
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	d7099ef3a0aa5bdae4f84c01c28f4711
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	fbdb4a0b2d76c6c616f8ac4a19820951
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	a03a08f9da5bd3c91dc92a14a691c4fa
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	4d2cc6197fb85415ba0d9d82fa0e4486
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	0a868e535a67489fbd4c4aba19c4dc18
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
