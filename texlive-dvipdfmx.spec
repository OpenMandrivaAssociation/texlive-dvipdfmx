# revision 26765
# category TLCore
# catalog-ctan /dviware/dvipdfmx/dvipdfmx.tar.gz
# catalog-date 2012-04-21 10:57:19 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-dvipdfmx
Version:	20120421
Release:	1
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
%{_texmfdir}/dvipdfmx/dvipdfmx.cfg
%{_texmfdir}/fonts/cmap/README
%{_texmfdir}/fonts/cmap/dvipdfmx/EUC-UCS2
%{_texmfdir}/fonts/cmap/dvipdfmx/README
%{_texmfdir}/fonts/cmap/dvipdfmx/UTF8-UCS2
%{_texmfdir}/fonts/map/dvipdfmx/cid-x.map
%{_texmfdir}/fonts/map/dvipdfmx/ckx.map
%{_texmfdir}/fonts/map/dvipdfmx/updmap/kanjix.map
%{_tlpkgdir}/tlpostcode/dvipdfmx.pl
%doc %{_texmfdir}/doc/dvipdfmx/dvipdfmx-special.pdf
%doc %{_texmfdir}/doc/dvipdfmx/dvipdfmx-special.tex
%doc %{_mandir}/man1/extractbb.1*
%doc %{_texmfdir}/doc/man/man1/extractbb.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/tlpostcode %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120421-1
+ Revision: 812238
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110322-5
+ Revision: 779438
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110322-4
+ Revision: 751218
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110322-3
+ Revision: 739747
- texlive-dvipdfmx

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110322-2
+ Revision: 729648
- texlive-dvipdfmx

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110322-1
+ Revision: 718282
- texlive-dvipdfmx
- texlive-dvipdfmx
- texlive-dvipdfmx
- texlive-dvipdfmx

