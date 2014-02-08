# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-cyrplain
Version:	20111103
Release:	3
Summary:	TeXLive cyrplain package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrplain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive cyrplain package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/cyrplain/README
%{_texmfdistdir}/tex/plain/cyrplain/cyramstx.ini
%{_texmfdistdir}/tex/plain/cyrplain/cyrblue.ini
%{_texmfdistdir}/tex/plain/cyrplain/cyrcmfnt.tex
%{_texmfdistdir}/tex/plain/cyrplain/cyrecfnt.tex
%{_texmfdistdir}/tex/plain/cyrplain/cyrtex.cfg
%{_texmfdistdir}/tex/plain/cyrplain/cyrtex.ini
%{_texmfdistdir}/tex/plain/cyrplain/cyrtex.tex
%{_texmfdistdir}/tex/plain/cyrplain/cyrtxinf.ini
%{_texmfdistdir}/tex/plain/cyrplain/makefmts.bat
%{_texmfdistdir}/tex/plain/cyrplain/makefmts.sh
%{_texmfdistdir}/tex/plain/cyrplain/plainenc.tex
%{_texmfdistdir}/tex/plain/cyrplain/txxdefs.tex
%{_texmfdistdir}/tex/plain/cyrplain/txxextra.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 750761
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718198
- texlive-cyrplain
- texlive-cyrplain
- texlive-cyrplain
- texlive-cyrplain

