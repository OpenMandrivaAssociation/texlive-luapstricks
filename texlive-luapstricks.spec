Name:		texlive-luapstricks
Version:	67207
Release:	1
Summary:	A PSTricks backend for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luapstricks
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapstricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapstricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables the use of PSTricks directly in LuaLaTeX
documents, without invoking external programmes, by
implementing a PostScript interpreter in Lua. Therefore it does
not require shell escape to be enabled or special environments,
and instead allows PSTricks to be used exactly like in dvips
based documents.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luapstricks
%{_texmfdistdir}/fonts/opentype/public/luapstricks
%doc %{_texmfdistdir}/doc/lualatex/luapstricks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
