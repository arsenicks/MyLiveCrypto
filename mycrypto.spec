Name:	mycrypto
Version:	3.12.0
Release:	2%{?dist}
Summary:	Packaged version of MyCrypto

License: MIT
URL:	https://github.com/MyCryptoHQ/mycrypto.com
Source0: https://github.com/MyCryptoHQ/mycrypto.com/releases/download/v%{version}/mycrypto-v%{version}.zip
Source1: https://github.com/arsenicks/MyLiveCrypto/blob/master/MyCrypto.desktop
Source2: https://github.com/MyCryptoHQ/mycrypto.com/blob/master/LICENSE

BuildArch: noarch
BuildRequires: desktop-file-utils

%description
MyCrypto is a free, open-source, client-side interface.
MyCrypto allow you to interact directly with the blockchain while remaining
 in full control of your keys & your funds.
You and only you are responsible for your security.

%prep
%setup -q -n mycrypto-v%{version}
%build
%install
install -d -m0755 %{buildroot}/usr/share/mycrypto
cp -av * %{buildroot}/usr/share/mycrypto

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

%files
%license LICENSE
%{_datadir}/mycrypto/
%{_datadir}/applications/MyCrypto.desktop
%doc

%changelog
* Wed Mar 21 2018 Rene Jr Purcell <arsenick@fedoraproject.org> - 3.12.0-1
- Initial spec file

* Thu Mar 22 2018 Rene Jr Purcell <arsenick@fedoraproject.org> - 3.12.0-2
- Added changelog
- Added license file
