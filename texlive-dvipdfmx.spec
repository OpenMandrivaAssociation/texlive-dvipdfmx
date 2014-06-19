# revision 33771
# category TLCore
# catalog-ctan /dviware/dvipdfmx/dvipdfmx.tar.gz
# catalog-date 2013-09-22 09:06:20 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-dvipdfmx
Version:	20130922
Release:	8
Summary:	An extended version of dvipdfm
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvipdfmx/dvipdfmx.tar.gz
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfmx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfmx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-glyphlist
Requires:	texlive-dvipdfmx-def
Requires:	texlive-dvipdfmx.bin

%description
Dvipdfmx (formerly dvipdfm-cjk) is a development of dvipdfm
created to support multi-byte character encodings and large
character sets for East Asian languages. Dvipdfmx, if "called"
with the name dvipdfm, operates in a "dvipdfm compatibility"
mode, so that users of the both packages need only keep one
executable. A secondary design goal is to support as many "PDF"
features as does pdfTeX. There being no documentation as such,
users are advised to consult the documentation of dvipdfm (as
well, of course, as the package Readme.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvipdfmx/dvipdfmx.cfg
%{_texmfdistdir}/fonts/cmap/dvipdfmx/EUC-UCS2
%{_texmfdistdir}/fonts/cmap/dvipdfmx/README
%{_texmfdistdir}/fonts/cmap/dvipdfmx/UTF8-UCS2
%{_texmfdistdir}/fonts/map/dvipdfmx/cid-x.map
%{_texmfdistdir}/fonts/map/dvipdfmx/ckx.map
%{_texmfdistdir}/fonts/map/dvipdfmx/updmap/kanjix.map
%{_tlpkgdir}/tlpostcode/dvipdfmx.pl
%doc %{_texmfdistdir}/doc/dvipdfm/Makefile
%doc %{_texmfdistdir}/doc/dvipdfm/dvipdfm.pdf
%doc %{_texmfdistdir}/doc/dvipdfm/dvipdfm.tex
%doc %{_texmfdistdir}/doc/dvipdfm/mwicks.bb
%doc %{_texmfdistdir}/doc/dvipdfm/mwicks.jpeg
%doc %{_texmfdistdir}/doc/dvipdfm/sample.tex
%doc %{_texmfdistdir}/doc/dvipdfm/something.bb
%doc %{_texmfdistdir}/doc/dvipdfm/something.eps
%doc %{_texmfdistdir}/doc/dvipdfm/something.fig
%doc %{_texmfdistdir}/doc/dvipdfm/something.pdf
%doc %{_texmfdistdir}/doc/dvipdfm/transistor.bb
%doc %{_texmfdistdir}/doc/dvipdfm/transistor.eps
%doc %{_texmfdistdir}/doc/dvipdfm/transistor.fig
%doc %{_texmfdistdir}/doc/dvipdfm/transistor.pdf
%doc %{_texmfdistdir}/doc/dvipdfmx/dvipdfmx-special.pdf
%doc %{_texmfdistdir}/doc/dvipdfmx/dvipdfmx-special.tex
%doc %{_mandir}/man1/dvipdfm.1*
%doc %{_texmfdistdir}/doc/man/man1/dvipdfm.man1.pdf
%doc %{_mandir}/man1/dvipdfmx.1*
%doc %{_texmfdistdir}/doc/man/man1/dvipdfmx.man1.pdf
%doc %{_mandir}/man1/dvipdft.1*
%doc %{_texmfdistdir}/doc/man/man1/dvipdft.man1.pdf
%doc %{_mandir}/man1/ebb.1*
%doc %{_texmfdistdir}/doc/man/man1/ebb.man1.pdf
%doc %{_mandir}/man1/extractbb.1*
%doc %{_texmfdistdir}/doc/man/man1/extractbb.man1.pdf
%doc %{_mandir}/man1/xdvipdfmx.1*
%doc %{_texmfdistdir}/doc/man/man1/xdvipdfmx.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/tlpostcode %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
