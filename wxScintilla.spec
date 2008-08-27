# TODO: optflags
#
# Conditional build:
%bcond_with	unicode		# use wx-gtk2-unicode-config instead of wx-gtk2-ansi-config
#
Summary:	wxScintilla - a wxWidgets implementation of the Scintilla editing control
Summary(pl.UTF-8):	wxScintilla - implementacja kontrolki Scintilla dla wxWidgets
Name:		wxScintilla
Version:	1.69.2
Release:	1
License:	wxWindows
Group:		Libraries
Source0:	http://dl.sourceforge.net/wxcode/wxscintilla_%{version}.tar.gz
# Source0-md5:	87c9ad26e576b59f37b4c36fc7aadb3c
URL:		http://wxcode.sourceforge.net/components/wxscintilla/
BuildRequires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	wxwidgets_ver	2.6

%description
wxScintilla implements the Scintilla editing control with the
wxWidgets API. It's derived from wxStyledTextCtrl (done by Robin Dunn)
and has the same functionality and a similar API. The almost singular
difference (beside naming) is it has a much faster release cycle.

%description -l pl.UTF-8
wxScintilla jest implementacją kontrolki edycyjnej Scintilla
wykorzystującą API wxWidgets. Jest rozwinięciem wxStyledTextCtrl
(napisanej przez Robina Dunna) i posiada taką samą funkcjonalność oraz
zbliżone API. Niemalże jedyną różnicą (poza nazwą) jest znacznie
szybszy cykl wydawania nowych wersji.

%package devel
Summary:	Header files for wxScintilla library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxScintilla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.1

%description devel
Header files for wxScintilla library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxScintilla.

%prep
%setup -q -n wxscintilla_%{version}

%build
%{__make} -C build \
	WXCONFIG=wx-gtk2-%{?with_unicode:unicode}%{!?with_unicode:ansi}-config

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/wx-%{wxwidgets_ver}/wx}

install lib/libwxscintilla.so $RPM_BUILD_ROOT%{_libdir}
install include/wx/*.h $RPM_BUILD_ROOT%{_includedir}/wx-%{wxwidgets_ver}/wx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/wx-%{wxwidgets_ver}/wx/*.h
