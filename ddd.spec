Summary:	A GUI for several command-line debuggers
Name:		ddd
Version:	3.3.12
Release:	4
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
BuildRequires:	pkgconfig(ncurses)
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
export CC=gcc
export CXX=g++
CXXFLAGS="%{optflags} -fpermissive"
%configure
%make X_INCLUDE="" RPATH=""

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


%changelog
* Mon Jun 04 2012 Andrey Bondrov <abondrov@mandriva.org> 3.3.12-3
+ Revision: 802370
- Drop some legacy junk

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.12-2mdv2011.0
+ Revision: 610213
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 3.3.12-1mdv2010.1
+ Revision: 508123
- fix build with gcc 4.3

* Thu Feb 12 2009 Frederik Himpe <fhimpe@mandriva.org> 3.3.12-1mdv2009.1
+ Revision: 339909
- Update to new version 3.3.12
- Don't do libtool magick in SPEC file, it's not needed anymore
- Use included desktop file instead of our custom one, but include
  Debugger category

* Fri Nov 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.3.11-6mdv2009.1
+ Revision: 303117
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 3.3.11-5mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 3.3.11-5mdv2008.0
+ Revision: 70180
- info file must be unregistered before being uninstalled

* Wed Jul 18 2007 Adam Williamson <awilliamson@mandriva.org> 3.3.11-4mdv2008.0
+ Revision: 53333
- rebuild with new lesstif
- create .desktop file in the spec, don't source it
- drop old menu and X-Mandriva category
- specify license as GPLv2

  + Ademar de Souza Reis Jr <ademar@mandriva.com.br>
    - Import ddd



* Tue Aug 29 2006 Götz Waschk <waschk@mandriva.org> 3.3.11-3mdv2007.0
- xdg menu

* Wed Sep 21 2005 Götz Waschk <waschk@mandriva.org> 3.3.11-2mdk
- replace prereq
- fix C++ flags

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 3.3.11-1mdk
- fix the source URL
- new version

* Sat Apr 09 2005 Olivier Thauvin <nanardon@mandrake.org> 3.3.10-2mdk
- adjust buildrequires for 64bits arch

* Wed Dec 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.10-1mdk
- 3.3.10

* Wed Aug 25 2004 Götz Waschk <waschk@linux-mandrake.com> 3.3.9-2mdk
- fix buildrequires

* Tue Aug 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.9-1mdk
- 3.3.9

* Fri Jun  4 2004 Stew Benedict <sbenedict@mandrakesoft.com> 3.3.8-2mdk
- rebuild, new gcc, libstdc++, add -fpermissive to CXXFLAGS
- remove rpath from binary, fix menu entry

* Fri Nov 14 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.3.8-1mdk
- 3.3.8

* Mon Oct 20 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.3.7-1mdk
- 3.3.7

* Fri Jun 20 2003 Götz Waschk <waschk@linux-mandrake.com> 3.3.6-2mdk
- fix buildrequires: readline-devel and binutils-devel (for -liberty)

* Wed Jun  4 2003 Götz Waschk <waschk@linux-mandrake.com> 3.3.6-1mdk
- update doc file listing
- drop pydb, seems to be missing
- drop source 1 (merged into main tarball)
- fix configure macro
- drop the patch
- fix buildrequires
- new version (the fork from sourceforge)

* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.3.1-9mdk
- rebuild for new glibc/rpm, installed but unpackaged files

* Thu Aug 15 2002 Laurent Culioli <laurent@pschit.net> 3.3.1-8mdk
- Rebuild with gcc3.2

* Wed Aug  7 2002 Götz Waschk <waschk@linux-mandrake.com> 3.3.1-7mdk
- gcc 3.2 build

* Thu Jul 25 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.3.1-6mdk
- rebuild with latest lesstif to address corrupted display

* Tue Jul 16 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.3.1-5mdk
- LessTif includes and libraries are in normal locations now

* Tue May 28 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.3.1-4mdk
- rebuild with gcc 3.1

* Tue Mar 26 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.3.1-3mdk
- add desktop file
- spec cleaning:
	- remove uneeded "rm -f $$RPM_BUILD_ROOT/%%_infodir/dir"
	- remove uneeded sub sheels usage
	- merge all mkdir -p $RPM_BUILD_ROOT%%_???dir
- better summary
- add BuildRequires
- fix for gcc3

* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Fix menu entry

* Thu Jun 21 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.3.1-1mdk
- Rework/Sanetize the package.
- 3.3.1.

* Sun Mar 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.3-3mdk
- fix files section

* Wed Feb 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.3-2mdk
- fixes descompression of doc (thx Ryan T. Sammartino)

* Tue Feb 13 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.3-1mdk
- updated to 3.3

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-3mdk
- ifarch ppc

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-2mdk
- disabled athena widgets

* Thu Sep 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-1mdk
- updated to 3.2.1
- add doc
- bm & macros

* Thu Jan 20 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs 
- used srpm provided by Dara Hazeghi <dhazeghi@pacbell.net>
