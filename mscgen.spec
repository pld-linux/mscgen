Summary:	mscgen - Message Sequence Chart Renderer
Summary(pl.UTF-8):	mscgen - narzędzie do renderowania wykresów z formatu MSC
Name:		mscgen
Version:	0.20
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://www.mcternan.me.uk/mscgen/software/%{name}-src-%{version}.tar.gz
# Source0-md5:	65c90fb5150d7176b65b793f0faa7377
URL:		http://www.mcternan.me.uk/mscgen/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gd-devel >= 2.0.22
BuildRequires:	pkgconfig
Requires:	gd >= 2.0.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mscgen is a small program that parses Message Sequence Chart
descriptions and produces PNG, EPS, SVG or server side image maps
(ismaps) as the output. Message Sequence Charts (MSCs) are a way of
representing entities and interactions over some time period and are
often used in combination with SDL. MSCs are popular in Telecoms to
specify how protocols operate although MSCs need not be complicated to
create or use. Mscgen aims to provide a simple text language that is
clear to create, edit and understand, which can also be transformed
into images.

%description -l pl.UTF-8
Mscgen to mały program analizujący opisy w formacie MSC (Message
Sequence Chart) i tworzący na wyjściu obrazy w formacie PNG, EPS, SVG
lub map po stronie serwera (ismap). Message Sequence Chart (wykresy
sekwencji komunikatów) to sposób reprezentowania encji i interakcji w
czasie, często używany w połączeniu z SDL. Wykresy MSC są popularne
przy telekomunikacji do określenia sposobu działania protokołów, ale
nie muszą być skomplikowane przy tworzeniu i wykorzystywaniu. Celem
mscgen jest zapewnienie prostego języka tekstowego, prostego do
zapisu, modyfikowania i rozumienia, a także nadającego się do
przekształcenia w obrazki.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mscgen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO examples/*.msc
%attr(755,root,root) %{_bindir}/mscgen
%{_mandir}/man1/mscgen.1*
