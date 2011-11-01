Name:		texlive-cyrplain
Version:	20111101
Release:	1
Summary:	TeXLive cyrplain package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrplain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive cyrplain package.

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
