%global tl_name luapstricks
%global tl_revision 79280

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12
Release:	%{tl_revision}.1
Summary:	A PSTricks backend for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/luapstricks
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luapstricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luapstricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the use of PSTricks directly in LuaLaTeX documents,
without invoking external programmes, by implementing a PostScript
interpreter in Lua. Therefore it does not require shell escape to be
enabled or special environments, and instead allows PSTricks to be used
exactly like in dvips based documents.

