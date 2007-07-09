Summary: 	A GUI for several command-line debuggers
Name:		ddd
Version:	3.3.11
Release: 	%mkrel 3
Source: 	http://prdownloads.sourceforge.net/ddd/%name-%version.tar.bz2
Source2:	ddd.desktop
Source3:	debugger16.png
Source4:	debugger22.png
Group: 		Development/Other
URL: 		http://www.gnu.org/software/ddd/
BuildRoot: 	%_tmppath/%name-buildroot
License: 	GPL
Requires(post): info-install
Requires(postun): info-install
BuildRequires: 	lesstif-devel
BuildRequires:  flex
BuildRequires:  readline-devel
BuildRequires:  libtermcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  binutils-devel
BuildRequires:  chrpath
Requires: 	lesstif, gdb

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

%build
cp -f /usr/share/libtool/config.* .
CXXFLAGS="$RPM_OPT_FLAGS -fpermissive"
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT{%_bindir,%_docdir,%_menudir}
%makeinstall

install -m 644 %SOURCE2 -D %buildroot%_datadir/applications/ddd.desktop 
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/{16x16,22x22}/apps
install -m 644 %SOURCE3 $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps/ddd.png
install -m 644 %SOURCE4 $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps/ddd.png

#install -m 755 pydb/pydb.py $RPM_BUILD_ROOT/%_bindir
#install -m 755 pydb/pydbcmd.py $RPM_BUILD_ROOT/%_bindir
#install -m 755 pydb/pydbsupt.py $RPM_BUILD_ROOT/%_bindir

#cd $RPM_BUILD_ROOT%{_bindir}
#ln -sf pydb.py pydb

cat > $RPM_BUILD_ROOT%_menudir/%name <<EOF
?package(%name):\
command="/usr/bin/ddd"\
title="Ddd"\
longtitle="Data Display Debugger"\
needs="x11"\
icon="development_section.png"\
section="More Applications/Development/Other" xdg="true"
EOF

# (sb) remove rpath from binary
chrpath -d $RPM_BUILD_ROOT/%{_bindir}/%{name}

# (sb) unpackaged files
rm -f $RPM_BUILD_ROOT/%{_libdir}/libiberty.a

%post
%_install_info %name.info
%update_menus
%update_icon_cache hicolor
 
%postun
%_remove_install_info %name.info
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README TODO TIPS NEWS AUTHORS doc/*pdf doc/html
%_bindir/*
%_mandir/*/*
%_infodir/%name.*
%_infodir/%name-*

%_menudir/*
%dir %_datadir/%name-%version
%_datadir/applications/ddd.desktop
%_datadir/%name-%version/COPYING
%_datadir/%name-%version/NEWS
%_datadir/%name-%version/ddd
%_datadir/%name-%version/themes
%_datadir/%name-%version/vsllib
%_datadir/icons/hicolor/*/apps/ddd.png
