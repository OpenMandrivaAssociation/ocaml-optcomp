Name:           ocaml-optcomp
Version:        1.1
Release:        %mkrel 1
Summary:        Optional compilation with cpp-like directives for OCaml
License:        BSD3
Group:          Development/Other
Source0:        https://forge.ocamlcore.org/frs/download.php/111/optcomp-%{version}.tar.gz
URL:            https://forge.ocamlcore.org/projects/optcomp/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  camlp4
###BuildRequires:  ocaml-findlib
BuildRequires:      findlib

%description
Optcomp is a camlp4 syntax extension which handles #if, #else, etc
directives in ocaml source files.

The difference between cpp and optcomp is that optcomp is more
caml-friendly than cpp:

 * it does not interpret "//", "/*", and "*/" as comment delimiters
 * it does not complains about missing "'"
 * it is easier to integrate in the build process when using other
   camlp4 syntax extensions

By the way optcomp does not do macro expansion while cpp does.

The difference between pa_macro and optcomp is that optcomp does not
require code that will be dropped to be valid caml code. So for
example some code that will be rejected by camlp4+pa_macro will be
accepted by camlp4+optcomp.

You can use optcomp with ocamlfind, with the package optcomp or you
can directly include it in your project.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n optcomp-%{version}

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/optcomp
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_libdir}/ocaml/optcomp
%{_libdir}/ocaml/optcomp/META
%{_libdir}/ocaml/optcomp/*.cmo

%files devel
%doc LICENSE README VERSION CHANGES CHANGES.darcs
%defattr(-,root,root)
%{_libdir}/ocaml/optcomp/*.ml*

