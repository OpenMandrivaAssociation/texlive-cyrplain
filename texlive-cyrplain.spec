%global tl_name cyrplain
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for using T2 encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/t2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrplain.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The T2 bundle provides a variety of separate support functions for using
Cyrillic characters in LaTeX: the mathtext package, for using Cyrillic
letters 'transparently' in formulae; the citehack package, for using
Cyrillic (or indeed any non-ascii) characters in citation keys; support
for Cyrillic in BibTeX; support for Cyrillic in Makeindex; and various
items of font support.

