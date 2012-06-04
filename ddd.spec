Summary:	A GUI for several command-line debuggers
Name:		ddd
Version:	3.3.12
Release:	3
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source3:	debugger16.png
Source4:	debugger22.png
Patch0:		ddd-3.3.12-gcc4.3.patch
Group:		Development/Other
URL:		http://www.gnu.org/software/ddd/
License:	GPLv2
BuildRequires:	lesstif-devel
BuildRequires:	flex
BuildRequires:	readline-devel
BuildRequires:	libtermcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	binutils-devel
BuildRequires:	chrpath
Requires:	lesstif
Requires:	gdb

%description
The Data Display Debugger (DDD) is a popular GUI for command-line
debuggers like GDB, DBX, JDB, WDB, XDB, the Perl debugger, and the
Python debugger.  DDD allows you to view source texts and provides an
interactive graphical data display, in which data structures are
displayed as graphs.  You can use your mouse to dereference pointers
or view structure contents, which are updated every time the program
stops.  DDD can debug programs written in Ada, C, C++, Chill, Fortran,
Java, Modula, Pascal, Perl, and Python.  DDD provides machine-level
debugging; hypertext source navigation and lookup; breakpoint,
watchpoint, backtrace, and history editors; array plots; undo and
redo; preferences and settings editors; program execution in the
terminal emulation window, debugging on a remote host, an on-line
manual, extensive help on the Motif user interface, and a command-line
interface with full editing, history and completion capabilities.

%prep
%setup -q
%patch0 -p0
sed -i -e "s/^Categories=Development;$/Categories=Development;Debugger;/" ddd/ddd.desktop

%build
CXXFLAGS="%{optflags} -fpermissive"
%configure2_5x
%make X_INCLUDE=""

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_bindir},%{_docdir}}
%makeinstall

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,22x22}/apps
install -m 644 %{SOURCE3} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/ddd.png
install -m 644 %{SOURCE4} %{buildroot}%{_iconsdir}/hicolor/22x22/apps/ddd.png

# (sb) remove rpath from binary
chrpath -d %{buildroot}%{_bindir}/%{name}

# (sb) unpackaged files
rm -f %{buildroot}%{_libdir}/libiberty.a

%files
%doc README TODO TIPS NEWS AUTHORS doc/*pdf doc/html
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/%{name}.*
%{_infodir}/%{name}-*
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-%{version}/COPYING
%{_datadir}/%{name}-%{version}/NEWS
%{_datadir}/%{name}-%{version}/ddd
%{_datadir}/%{name}-%{version}/themes
%{_datadir}/%{name}-%{version}/vsllib
%{_iconsdir}/hicolor/*/apps/ddd.png
