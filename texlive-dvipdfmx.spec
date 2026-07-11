%global tl_name dvipdfmx
%global tl_revision 78409

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An extended version of dvipdfm
Group:		Publishing
URL:		https://www.ctan.org/pkg/dvipdfmx
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfmx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfmx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvipdfmx.bin)
Requires:	texlive(extractbb)
Requires:	texlive(glyphlist)
Requires:	texlive(texlive-scripts-extra)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Dvipdfmx (formerly dvipdfm-cjk) is a development of dvipdfm created to
support multi-byte character encodings and large character sets for East
Asian languages. Dvipdfmx, if "called" with the name dvipdfm, operates
in a "dvipdfm compatibility" mode, so that users of the both packages
need only keep one executable. A secondary design goal is to support as
many "PDF" features as does pdfTeX. The current version of the package
is no longer maintained on CTAN as a separate entity; development now
takes place within the TeX Live framework, and it is no longer available
as a separate package. For download, support, and other information,
please see TeX Live. However, the information on this page is maintained
and should be current.

