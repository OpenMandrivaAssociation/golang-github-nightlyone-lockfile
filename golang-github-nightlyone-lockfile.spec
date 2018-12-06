# https://github.com/nightlyone/lockfile
%global goipath         github.com/nightlyone/lockfile
%global commit          e83dc5e7bba095e8d32fb2124714bf41f2a30cb5

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Handle locking via pid files
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml



%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch


%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gite83dc5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.20180315gite83dc5e
- Upload glide files

* Thu Mar 15 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gite83dc5e
- First package for Fedora
  resolves: #1556915
