%define pkg_release 0.1.5


Name:          fedora-kernel-manager
Version:       %{pkg_release}
Release:       3%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       A Libadwaita rust based application for managing and installing kernels.


URL:            https://github.com/CosmicFusion/fedora-kernel-manager
Source0:        %{URL}/releases/download/%{pkg_release}/fedora-kernel-manager.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:	wget
BuildRequires:	cargo
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gtk4-devel
BuildRequires:	gtk3-devel
BuildRequires:	libadwaita-devel
BuildRequires:	openssl-devel
BuildRequires:	llvm-devel
BuildRequires:	clang-devel

Requires:   /usr/bin/bash
Requires:	gtk4
Requires:	gtk3
Requires:	libadwaita
Requires: 	glib2
Requires: 	util-linux
Requires: 	polkit
Requires:   iputils

Recommends: scx-scheds

%description
A Libadwaita rust based application for managing and installing kernels.

%prep
%autosetup -p1 -n fedora-kernel-manager

%build
DESTDIR=%{buildroot} make install

%files
%{_prefix}/lib/fedora-kernel-manager/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/polkit-1/actions/fkm.change.scx.policy
%{_datadir}/polkit-1/actions/fkm.modify.package.policy
%{_prefix}/lib/fedora-kernel-manager/kernel_branches/kernel.json
%exclude %{_prefix}/lib/fedora-kernel-manager/kernel_branches/kernel-cachyos.json
%exclude %{_prefix}/lib/fedora-kernel-manager/scripts/kernel-cachyos-init.sh
%exclude %{_datadir}/polkit-1/actions/fkm.kernel.cachyos.init.policy
%exclude %{_datadir}/polkit-1/rules.d/99-fkm.kernel.cachyos.init.rules

