# revision 25890
# category Package
# catalog-ctan /fonts/libertineotf
# catalog-date 2012-04-08 14:50:51 +0200
# catalog-license gpl2
# catalog-version 5.13-8
Name:		texlive-libertineotf
Version:	5.13.8
Release:	12
Summary:	Linux Libertine fonts for use with lua(La)TeX and xe(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertineotf
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertineotf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertineotf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertineotf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Linux-Libertine project offers a font family with a wide
range of shapes, and support of several alphabets (including
Latin, Cyrillic, Greek and Hebrew). This bundle provides the
fonts in OpenType format (see libertine-legacy for an earlier
release in Adobe Type 1 format).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_K.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_R.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_RB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_RI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aBL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aU.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aUB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aUI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aUL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aULB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aW.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aWB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aWI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aWL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinBiolinum_aWLB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_DR.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_I.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_R.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_RB.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_RBI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_RI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_RZ.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_RZI.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_aBL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_aDRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_aRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinLibertine_aZL.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinMono_M.otf
%{_texmfdistdir}/fonts/opentype/public/libertineotf/LinMono_aML.otf
%{_texmfdistdir}/tex/latex/libertineotf/fxbuni.inc
%{_texmfdistdir}/tex/latex/libertineotf/fxiuni.inc
%{_texmfdistdir}/tex/latex/libertineotf/fxkuni.inc
%{_texmfdistdir}/tex/latex/libertineotf/fxluni.inc
%{_texmfdistdir}/tex/latex/libertineotf/libertineotf.sty
%doc %{_texmfdistdir}/doc/fonts/libertineotf/GPL.txt
%doc %{_texmfdistdir}/doc/fonts/libertineotf/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/libertineotf/README
%doc %{_texmfdistdir}/doc/fonts/libertineotf/libertine.pdf
%doc %{_texmfdistdir}/doc/fonts/libertineotf/lppl.txt
#- source
%doc %{_texmfdistdir}/source/fonts/libertineotf/LinBiolinumO-gpos.csv
%doc %{_texmfdistdir}/source/fonts/libertineotf/LinBiolinumO-gsub.csv
%doc %{_texmfdistdir}/source/fonts/libertineotf/LinLibertineO-gpos.csv
%doc %{_texmfdistdir}/source/fonts/libertineotf/LinLibertineO-gsub.csv
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_01.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_02.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_03.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_04.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_05.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/lib_bsp_06.tex
%doc %{_texmfdistdir}/source/fonts/libertineotf/libertine.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.13.8-1
+ Revision: 790646
- Import texlive-libertineotf
- Import texlive-libertineotf

