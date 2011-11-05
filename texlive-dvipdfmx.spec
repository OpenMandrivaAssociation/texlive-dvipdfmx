# revision 23089
# category TLCore
# catalog-ctan /dviware/dvipdfmx/dvipdfmx.tar.gz
# catalog-date 2011-03-22 20:35:08 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-dvipdfmx
Version:	20110322
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdir}/dvipdfmx/dvipdfmx.cfg
%{_texmfdir}/fonts/cmap/README
%{_texmfdir}/fonts/cmap/dvipdfmx/EUC-UCS2
%{_texmfdir}/fonts/cmap/dvipdfmx/README
%{_texmfdir}/fonts/map/dvipdfmx/cid-x.map
%doc %{_texmfdir}/doc/dvipdfmx/dvipdfmx-special.pdf
%doc %{_texmfdir}/doc/dvipdfmx/dvipdfmx-special.tex
%doc %{_mandir}/man1/extractbb.1*
%doc %{_texmfdir}/doc/man/man1/extractbb.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
