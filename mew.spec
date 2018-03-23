Name:	etherwallet
Version:	3.21.02
Release:	2%{?dist}
Summary:	Packaged version of MyEtherWallet

License: MIT
URL:	https://github.com/kvhnuke/etherwallet	
Source0: https://github.com/kvhnuke/etherwallet/releases/download/v%{version}/etherwallet-v%{version}.zip
Source1: https://github.com/arsenicks/MyLiveCrypto/blob/master/MyEtherWallet.desktop
Source2: https://github.com/kvhnuke/etherwallet/blob/mercury/LICENSE.md

BuildArch: noarch
BuildRequires: desktop-file-utils

%description
MyEtherWallet is a free, open-source, client-side tool for easily & securely 
interacting with the Ethereum network. As one of the leading providers of
Ethereum services, MyEtherWallet equips users with an easy-to-understand and
 accessible suite of tools for their needs.

It was created and is maintained by kvhnuke and tayvano.

%prep
%setup -q -n etherwallet-v%{version}
%build

%install
install -d -m0755 %{buildroot}/usr/share/mew/
cp -av * %{buildroot}/usr/share/mew/

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

%files
%license %{_datadir}/LICENSE.md
%{_datadir}/mew/
%{_datadir}/applications/MyEtherWallet.desktop
%doc

%changelog
* Thu Mar 22 2018 Rene Jr Purcell <arsenick@fedoraproject.org> - 3.21.02-2
- Added changelog
- Added license file

* Mon Mar 19 2018 Rene Jr Purcell <arsenick@fedoraproject.org> - 3.21.02-1
- Initial spec file


