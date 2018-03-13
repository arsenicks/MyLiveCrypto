#Name:	MyEtherWallet	
Name:	etherwallet
Version:	3.20.03
Release:	1%{?dist}
Summary:	Packaged version of MEW. Package maintained by Rene Jr Purcell

Group:	Applications/System	
License: MIT License	
URL:	https://github.com/kvhnuke/etherwallet	
Source0: https://github.com/kvhnuke/etherwallet/releases/download/v%{version}/etherwallet-v%{version}.zip
Source1: MyEtherWallet.desktop

BuildRoot: %{_tmppath}/%{name}-v%{version}-root
BuildArch: noarch
BuildRequires: desktop-file-utils

Requires: firefox

%description
MyEtherWallet is a free, open-source, client-side tool for easily & securely interacting with the Ethereum network. 
As one of the leading providers of Ethereum services,
MyEtherWallet equips users with an easy-to-understand and accessible suite of tools for their needs.

It was created and is maintained by kvhnuke and tayvano.

%prep
%setup -q -n etherwallet-v%{version}



%build


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}/usr/share/mew/
%{__cp} -av * %{buildroot}/usr/share/mew/

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

#cat > %{buildroot}/usr/share/mew/MyEtherWallet.desktop <<'EOF'
#[Desktop Entry]
#Name=MyEtherWallet
#Comment=MyEtherWallet is a free, open-source, client-side tool for easily & securely interacting with the Ethereum network.
#Exec=brave /usr/share/mew/index.html
#Icon=/usr/share/mew/images/myetherwallet-logo-square.png
#Categories=Application;Network;X-Red-Hat-Base;
#Type=Application
#Terminal=0
#X-Desktop-File-Install-Version=0.3
#EOF

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/share/mew/
%doc
%{_datadir}/applications/MyEtherWallet.desktop




%changelog
