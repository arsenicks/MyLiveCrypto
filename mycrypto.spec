Name:	mycrypto
Version:	3.12.0
Release:	1%{?dist}
Summary:	Packaged version of MyCrypto. Package maintained by Rene Jr Purcell

Group:	Applications/System	
License: MIT License	
URL:	https://github.com/MyCryptoHQ/mycrypto.com
Source0: https://github.com/MyCryptoHQ/mycrypto.com/releases/download/v%{version}/mycrypto-v%{version}.zip
Source1: MyCrypto.desktop

BuildRoot: %{_tmppath}/%{name}-v%{version}-root
BuildArch: noarch
BuildRequires: desktop-file-utils


Requires: firefox

%description
MyCrypto is a free, open-source, client-side interface.
MyCrypto allow you to interact directly with the blockchain while remaining in full control of your keys & your funds.
You and only you are responsible for your security.

%prep
%setup -q -n mycrypto-v%{version}



%build


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}/usr/share/mycrypto
%{__cp} -av * %{buildroot}/usr/share/mycrypto

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/share/mycrypto/
%doc
%{_datadir}/applications/MyCrypto.desktop




%changelog

