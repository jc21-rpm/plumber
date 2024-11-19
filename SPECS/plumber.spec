%define debug_package %{nil}

%global gh_user batchcorp

Name:           plumber
Version:        2.8.0
Release:        1%{?dist}
Summary:        A swiss army knife CLI tool for interacting with Kafka, RabbitMQ and other messaging systems.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
plumber is a CLI devtool for inspecting, piping, messaging and redirecting data
in message systems like Kafka, RabbitMQ , GCP PubSub and many more.

%prep
%setup -q -n %{name}-%{version}

%build
make test
make build/linux

%install
install -Dm0755 build/%{name}-linux %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE

%changelog
* Tue Nov 19 2024 Jamie Curnow <jc@jc21.com> 2.8.0-1
- https://github.com/batchcorp/plumber/releases/tag/v2.8.0

* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 2.7.0-1
- https://github.com/batchcorp/plumber/releases/tag/v2.7.0

* Mon Feb 13 2023 Jamie Curnow <jc@jc21.com> 2.0.0-1
- https://github.com/batchcorp/plumber/releases/tag/v2.0.0
