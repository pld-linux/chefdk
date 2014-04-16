# NOTE
# - this package by upstream is bundle (345M download, 1.5G unpacked) of all dependencies plus new tool called 'chef'
Summary:	Chef Development Kit
Name:		chefdk
Version:	0.0.1
Release:	0.1
License:	Apache v2.0
Group:		Networking/Admin
Source0:	https://github.com/opscode/chef-dk/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	80f274de84f339971e7afa0de463a842
URL:		http://docs.opscode.com/ctl_chef.html
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	sed >= 4.0
%if %{with tests}
%endif
Requires:	berkshelf
Requires:	chef
Requires:	chef-spec
Requires:	foodcritic
Requires:	knife
Requires:	ruby(abi) >= 2.0
Requires:	test-kitchen
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef Development Kit (Chef DK) brings Chef and the development tools
developed by the Chef Community together and acts as the consistent
interface to this awesomeness.

This awesomeness is composed of:
- chef
- berkshelf
- test-kitchen
- ChefSpec
- foodcritic

%prep
%setup -q -n chef-dk-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md CHANGELOG.md
%attr(755,root,root) %{_bindir}/chef
%{ruby_vendorlibdir}/chef-dk.rb
%{ruby_vendorlibdir}/chef-dk
