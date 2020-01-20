%define package_puppetverify 0

%if 0%{?rhel}
%define package_yum_updatesd 0
%else
%define package_yum_updatesd 1
%endif

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pluginhome /usr/lib/yum-plugins

Summary: Utilities based around the yum package manager
Name: yum-utils
Version: 1.1.31
Release: 42%{?dist}
License: GPLv2+
Group: Development/Tools
Source: http://yum.baseurl.org/download/yum-utils/%{name}-%{version}.tar.gz
Patch1: yum-utils-HEAD.patch
Patch2: BZ-1002491-remove-security-plugin.patch
Patch3: BZ-1050218-YumBaseError-not-defined.patch
Patch4: BZ-1052871-debuginfo-install-wrong-repo-suffix.patch
Patch5: BZ-1024070-yum-builddep-requires-source-repos-disabled.patch
Patch6: BZ-1060702-reposync-nonexistent-repo.patch
Patch7: BZ-1082050-source-repos.patch

# rhel-7.1
Patch50: BZ-1134989-post-transaction-actions-allow-colons.patch
Patch51: BZ-1133125-reposync-urls-for-all-repos.patch
Patch52: BZ-1129590-setopt-wildcards-save.patch
Patch53: BZ-1127782-post-transaction-action.patch
Patch54: BZ-1121714-reposync-manpage-missing-switches.patch
Patch55: BZ-1113391-yumdownloader-depsolving-errors.patch
Patch56: BZ-1104995-yumdownloader-redownloading-existing-rpms.patch
Patch57: BZ-1095150-needs-restarting-fixes.patch
Patch58: BZ-1139032-reposync-directory-structure.patch
Patch59: BZ-1140864-reposync-urls-option-ignores-downloaded.patch
Patch60: BZ-1107658-needs-restarting-graceful-error.patch

#rhel-7.2
Patch100: BZ-1075708-yum-config-manager-config-file-update.patch
Patch101: BZ-1151154-yum-config-manager-disable-all-repos.patch
Patch102: BZ-1213602-overlayfs-workaround-plugin.patch
Patch103: BZ-817046-yum-builddep-respect-tolerant-ignore-missing-reqs.patch

#rhel-7.3
Patch120: BZ-1293707-debuginfo-installonly-latest-version.patch
Patch121: BZ-1184912-yum-config-manager-fix-add-repo.patch
Patch122: BZ-1091698-fs-snapshot-obsolete-btrfsctl.patch
Patch123: BZ-1285750-repoquery-version.patch
Patch124: BZ-1269414-yum-plugin-priorities-obsoletes.patch
Patch125: BZ-1264774-archlist-docs.patch
Patch126: BZ-1156057-yum-builddep-manpage-arched-requires.patch
Patch127: BZ-1245117-yum-config-manager-all-repos.patch
Patch128: BZ-1296282-verifytree-fix-comps-schema.patch
Patch129: BZ-1192946-needs-restarting-add-reboothint-opt.patch
Patch130: BZ-1335587-needs-restarting-add-services-opt.patch
Patch131: BZ-1329649-reposync-download-metadata-manpage.patch

#rhel-7.4
Patch150: BZ-1403015-yum-config-manager-select-disabled-repoid-setopts.patch
Patch151: BZ-1406891-verify-exit-status.patch
Patch152: BZ-1429831-yum-copr.patch

URL: http://yum.baseurl.org/download/yum-utils/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
# For new findRepos() API and utils.get_process_info() API.
Requires: yum >= 3.4.3-143, libxml2-python
Requires: python-kitchen
BuildRequires: python-devel >= 2.4
BuildRequires: gettext
BuildRequires: intltool
Provides: yum-utils-translations = %{version}-%{release}


%description
yum-utils is a collection of utilities and examples for the yum package
manager. It includes utilities by different authors that make yum easier and
more powerful to use. These tools include: debuginfo-install, 
find-repos-of-install, needs-restarting, package-cleanup, repoclosure, 
repodiff, repo-graph, repomanage, repoquery, repo-rss, reposync,
repotrack, show-installed, show-changed-rco, verifytree, yumdownloader,
yum-builddep, yum-complete-transaction, yum-config-manager, yum-debug-dump,
yum-debug-restore and yum-groups-manager.

%package -n yum-updateonboot
Summary: Run yum update on system boot
Group: System Environment/Base
Requires: python, yum >= 2.4
Requires(pre): chkconfig
Requires(post): chkconfig

%description -n yum-updateonboot
Runs yum update on system boot. This allows machines that have been turned
off for an extended amount of time to become secure immediately, instead of
waiting until the next early morning cron job.

%package -n yum-plugin-changelog
Summary: Yum plugin for viewing package changelogs before/after updating
Group: System Environment/Base
Provides: yum-changelog = %{version}-%{release}
Obsoletes: yum-changelog < 1.1.20-0
Conflicts: yum-changelog < 1.1.20-0
# changelog requires new update_md.UpdateMetadata() API in 3.2.23
Requires: yum >= 3.2.23
Requires: python-dateutil

%description -n yum-plugin-changelog
This plugin adds a command line option to allow viewing package changelog
deltas before or after updating packages.

%package -n yum-plugin-fastestmirror
Summary: Yum plugin which chooses fastest repository from a mirrorlist
Group: System Environment/Base
Provides: yum-fastestmirror = %{version}-%{release}
Obsoletes: yum-fastestmirror < 1.1.20-0
Conflicts: yum-fastestmirror < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-fastestmirror
This plugin sorts each repository's mirrorlist by connection speed
prior to downloading packages.

%package -n yum-plugin-protectbase
Summary: Yum plugin to protect packages from certain repositories.
Group: System Environment/Base
Provides: yum-protectbase = %{version}-%{release}
Obsoletes: yum-protectbase < 1.1.20-0
Conflicts: yum-protectbase < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-protectbase
This plugin allows certain repositories to be protected. Packages in the
protected repositories can't be overridden by packages in non-protected
repositories even if the non-protected repo has a later version.

%package -n yum-plugin-versionlock
Summary: Yum plugin to lock specified packages from being updated
Group: System Environment/Base
Provides: yum-versionlock = %{version}-%{release}
Obsoletes: yum-versionlock < 1.1.20-0
Conflicts: yum-versionlock < 1.1.20-0
Requires: yum >= 3.2.24

%description -n yum-plugin-versionlock
This plugin takes a set of name/versions for packages and excludes all other
versions of those packages (including optionally following obsoletes). This
allows you to protect packages from being updated by newer versions,
for example.

%package -n yum-plugin-tsflags
Summary: Yum plugin to add tsflags by a commandline option
Group: System Environment/Base
Provides: yum-tsflags = %{version}-%{release}
Obsoletes: yum-tsflags < 1.1.20-0
Conflicts: yum-tsflags < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-tsflags
This plugin allows you to specify optional transaction flags on the yum
command line

%package -n yum-plugin-priorities
Summary: plugin to give priorities to packages from different repos
Group: System Environment/Base
Provides: yum-priorities = %{version}-%{release}
Obsoletes: yum-priorities < 1.1.20-0
Conflicts: yum-priorities < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-priorities
This plugin allows repositories to have different priorities.
Packages in a repository with a lower priority can't be overridden by packages
from a repository with a higher priority even if repo has a later version.

%if %{package_yum_updatesd}
%package -n yum-plugin-refresh-updatesd
Summary: Tell yum-updatesd to check for updates when yum exits
Group: System Environment/Base
Provides: yum-refresh-updatesd = %{version}-%{release}
Obsoletes: yum-refresh-updatesd < 1.1.20-0
Conflicts: yum-refresh-updatesd < 1.1.20-0
Requires: yum >= 3.0
Requires: yum-updatesd

%description -n yum-plugin-refresh-updatesd
yum-refresh-updatesd tells yum-updatesd to check for updates when yum exits.
This way, if you run 'yum update' and install all available updates, puplet
will almost instantly update itself to reflect this.
%endif

%package -n yum-plugin-merge-conf
Summary: Yum plugin to merge configuration changes when installing packages
Group: System Environment/Base
Provides: yum-merge-conf = %{version}-%{release}
Obsoletes: yum-merge-conf < 1.1.20-0
Conflicts: yum-merge-conf < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-merge-conf
This yum plugin adds the "--merge-conf" command line option. With this option,
Yum will ask you what to do with config files which have changed on updating a
package.

%package -n yum-plugin-upgrade-helper
Summary: Yum plugin to help upgrades to the next distribution version
Group: System Environment/Base
Provides: yum-upgrade-helper = %{version}-%{release}
Obsoletes: yum-upgrade-helper < 1.1.20-0
Conflicts: yum-upgrade-helper < 1.1.20-0
Requires: yum >= 3.0

%description -n yum-plugin-upgrade-helper
this plugin allows yum to erase specific packages on install/update based on an additional
metadata file in repositories. It is used to simplify distribution upgrade hangups.

%package -n yum-plugin-aliases
Summary: Yum plugin to enable aliases filters
Group: System Environment/Base
Provides: yum-aliases = %{version}-%{release}
Obsoletes: yum-aliases < 1.1.20-0
Conflicts: yum-aliases < 1.1.20-0
# Requires args_hook
Requires: yum >= 3.2.23
Requires: yum-utils-translations = %{version}-%{release}

%description -n yum-plugin-aliases
This plugin adds the command alias, and parses the aliases config. file to
enable aliases.

%package -n yum-plugin-list-data
Summary: Yum plugin to list aggregate package data
Group: System Environment/Base
Provides: yum-list-data = %{version}-%{release}
Obsoletes: yum-list-data < 1.1.20-0
Conflicts: yum-list-data < 1.1.20-0
Requires: yum >= 3.0.5

%description -n yum-plugin-list-data
This plugin adds the commands list- vendors, groups, packagers, licenses,
arches, committers, buildhosts, baseurls, package-sizes, archive-sizes and
installed-sizes.

%package -n yum-plugin-filter-data
Summary: Yum plugin to list filter based on package data
Group: System Environment/Base
Provides: yum-filter-data = %{version}-%{release}
Obsoletes: yum-filter-data < 1.1.20-0
Conflicts: yum-filter-data < 1.1.20-0
Requires: yum >= 3.2.17

%description -n yum-plugin-filter-data
This plugin adds the options --filter- vendors, groups, packagers, licenses,
arches, committers, buildhosts, baseurls, package-sizes, archive-sizes and
installed-sizes. Note that each package must match at least one pattern/range in
each category, if any were specified.

%package -n yum-plugin-tmprepo
Summary: Yum plugin to add temporary repositories
Group: System Environment/Base
Provides: yum-tmprepo = %{version}-%{release}
Obsoletes: yum-tmprepo < 1.1.20-0
Conflicts: yum-tmprepo < 1.1.20-0
Requires: yum >= 3.2.11
Requires: createrepo

%description -n yum-plugin-tmprepo
This plugin adds the option --tmprepo which takes a url to a .repo file
downloads it and enables it for a single run. This plugin tries to ensure
that temporary repositories are safe to use, by default, by not allowing
gpg checking to be disabled.

%package -n yum-plugin-verify
Summary: Yum plugin to add verify command, and options
Group: System Environment/Base
Provides: yum-verify = %{version}-%{release}
Obsoletes: yum-verify < 1.1.20-0
Conflicts: yum-verify < 1.1.20-0
Requires: yum >= 3.2.12

%description -n yum-plugin-verify
This plugin adds the commands verify, verify-all and verify-rpm. There are
also a couple of options. This command works like rpm -V, to verify your
installation.

%package -n yum-plugin-keys
Summary: Yum plugin to deal with signing keys
Group: System Environment/Base
Provides: yum-keys = %{version}-%{release}
Obsoletes: yum-keys < 1.1.20-0
Conflicts: yum-keys < 1.1.20-0
Requires: yum >= 3.2.19

%description -n yum-plugin-keys
This plugin adds the commands keys, keys-info, keys-data and keys-remove. They
allow you to query and remove signing keys.

%package -n yum-plugin-remove-with-leaves
Summary: Yum plugin to remove dependencies which are no longer used because of a removal
Group: System Environment/Base
Provides: yum-remove-with-leaves = %{version}-%{release}
Obsoletes: yum-remove-with-leaves < 1.1.20-0
Conflicts: yum-remove-with-leaves < 1.1.20-0
Requires: yum >= 3.2.19

%description -n yum-plugin-remove-with-leaves
This plugin removes any unused dependencies that were brought in by an install
but would not normally be removed. It helps to keep a system clean of unused
libraries and packages.

%package -n yum-plugin-post-transaction-actions
Summary: Yum plugin to run arbitrary commands when certain pkgs are acted on
Group: System Environment/Base
Provides: yum-post-transaction-actions = %{version}-%{release}
Obsoletes: yum-post-transaction-actions < 1.1.20-0
Conflicts: yum-post-transaction-actions < 1.1.20-0
Requires: yum >= 3.2.19

%description -n yum-plugin-post-transaction-actions
This plugin allows the user to run arbitrary actions immediately following a
transaction when specified packages are changed.

%package -n yum-NetworkManager-dispatcher
Summary: NetworkManager script which tells yum to check its cache on network change
Group: System Environment/Base
Requires: yum >= 3.2.17

%description -n yum-NetworkManager-dispatcher
This NetworkManager "dispatch script" forces yum to check its cache if/when a
new network connection happens in NetworkManager. Note that currently there is
no checking of previous data, so if your WiFi keeps going up and down (or you
suspend/resume a lot) yum will recheck its cached data a lot.

%package -n yum-plugin-rpm-warm-cache
Summary: Yum plugin to access the rpmdb files early to warm up access to the db 
Group: System Environment/Base
Provides: yum-rpm-warm-cache = %{version}-%{release}
Obsoletes: yum-rpm-warm-cache < 1.1.20-0
Conflicts: yum-rpm-warm-cache < 1.1.20-0
Requires: yum >= 3.2.19

%description -n yum-plugin-rpm-warm-cache
This plugin reads the rpmdb files into the system cache before accessing the
rpmdb directly. In some cases this should speed up access to rpmdb information

%package -n yum-plugin-auto-update-debug-info
# Works by searching for *-debuginfo ... so it shouldn't trigger on itself.
Summary: Yum plugin to enable automatic updates to installed debuginfo packages
Group: System Environment/Base
Obsoletes: yum-plugin-auto-update-debuginfo < 1.1.21-0
Conflicts: yum-plugin-auto-update-debuginfo < 1.1.21-0
Provides: yum-plugin-auto-update-debuginfo = %{version}-%{release}
Requires: yum >= 3.2.19

%description -n yum-plugin-auto-update-debug-info
This plugin looks to see if any debuginfo packages are installed, and if there
are it enables all debuginfo repositories that are "children" of enabled
repositories.

%package -n yum-plugin-show-leaves
Summary: Yum plugin which shows newly installed leaf packages
Group: System Environment/Base
Requires: yum >= 3.2.23

%description -n yum-plugin-show-leaves
Yum plugin which shows newly installed leaf packages
and packages that became leaves after a transaction

%package -n yum-plugin-local
Summary: Yum plugin to automatically manage a local repo. of downloaded packages
Group: System Environment/Base
# Who the hell knows what version :)
Requires: yum >= 3.2.22
Requires: createrepo

%description -n yum-plugin-local
When this plugin is installed it will automatically copy all downloaded packages
to a repository on the local filesystem, and (re)build that repository. This
means that anything you've downloaded will always exist, even if the original
repo. removes it (and can thus. be reinstalled/downgraded/etc.).

%package -n yum-plugin-fs-snapshot
Summary: Yum plugin to automatically snapshot your filesystems during updates
Group: System Environment/Base
Requires: yum >= 3.2.22
Requires: btrfs-progs

%description -n yum-plugin-fs-snapshot
When this plugin is installed it will automatically snapshot any
filesystem that is touched by the packages in a yum update or yum remove.

%package -n yum-plugin-ps
Summary: Yum plugin to look at processes, with respect to packages
Group: System Environment/Base
Requires: yum >= 3.2.27

%description -n yum-plugin-ps
When this plugin is installed it adds the yum command "ps", which allows you
to see which running processes are accociated with which packages (and if they
need rebooting, or have updates, etc.)

%if %{package_puppetverify}
%package -n yum-plugin-puppetverify
Summary: Yum plugin to add puppet checksums to verify data
Group: System Environment/Base
Provides: yum-puppetverify = %{version}-%{release}
Requires: yum >= 3.2.12
Requires: PyYAML >= 3.09
Requires: puppet

%description -n yum-plugin-puppetverify
Supplies checksums for files in packages from puppet's state file. 
%endif

%package -n yum-plugin-copr
Summary: Yum plugin to add copr command
Group: System Environment/Base
Provides: yum-copr = %{version}-%{release}
Requires: yum >= 3.4.3
Requires: python-requests

%description -n yum-plugin-copr
This plugin adds the command copr, for adding/listing/searching copr repos.

%package -n yum-plugin-ovl
Summary: Yum plugin to work around overlayfs issues
Group: System Environment/Base
Provides: yum-ovl = %{version}-%{release}
Requires: yum >= 3.4.3

%description -n yum-plugin-ovl
This plugin touches rpmdb files to work around overlayfs issues.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# rhel-7.1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1

#rhel-7.2
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

#rhel-7.3
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1

#rhel-7.4
%patch150 -p1
%patch151 -p1
%patch152 -p1

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
make -C updateonboot DESTDIR=$RPM_BUILD_ROOT install

%find_lang %name

# Plugins to install
plugins="\
 changelog \
 fastestmirror \
 protectbase \
 versionlock \
 tsflags \
 priorities \
 merge-conf \
 upgrade-helper \
 aliases \
 list-data \
 filter-data \
 tmprepo \
 verify \
 keys \
 remove-with-leaves \
 post-transaction-actions \
 rpm-warm-cache \
 auto-update-debuginfo \
 show-leaves \
 local \
 fs-snapshot \
 ps \
 ovl \
 copr \
"
%if %{package_puppetverify}
plugins="$plugins \
 puppetverify \
"
%endif

%if %{package_yum_updatesd}
plugins="$plugins \
 refresh-updatesd \
"
%endif

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/ $RPM_BUILD_ROOT/%pluginhome
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/post-actions

cd plugins
for plug in $plugins; do
    install -m 644 $plug/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
    install -m 644 $plug/*.py $RPM_BUILD_ROOT/%pluginhome
    %{__python} -c "import compileall; compileall.compile_dir('$RPM_BUILD_ROOT/%pluginhome', 1)"
done
install -m 644 aliases/aliases $RPM_BUILD_ROOT/%{_sysconfdir}/yum/aliases.conf
install -m 644 versionlock/versionlock.list $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
# need for for the ghost in files section of yum-plugin-local
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum.repos.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/_local.repo


%clean
rm -rf $RPM_BUILD_ROOT

%post -n yum-updateonboot
/sbin/chkconfig --add yum-updateonboot >/dev/null 2>&1 || :;

%preun -n yum-updateonboot
if [ $1 = 0 ]; then
    /sbin/service yum-updateonboot stop >/dev/null 2>&1 || :;
    /sbin/chkconfig --del yum-updateonboot >/dev/null 2>&1 || :;
fi

%files -f %{name}.lang
%defattr(-, root, root)
%doc README yum-util-cli-template
%doc COPYING
%doc plugins/README
%{_sysconfdir}/bash_completion.d
%{_bindir}/debuginfo-install
%{_bindir}/find-repos-of-install
%{_bindir}/needs-restarting
%{_bindir}/package-cleanup
%{_bindir}/repoclosure
%{_bindir}/repodiff
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/repotrack
%{_bindir}/reposync
%{_bindir}/repo-graph
%{_bindir}/repo-rss
%{_bindir}/verifytree
%{_bindir}/yumdownloader
%{_bindir}/yum-builddep
%{_bindir}/yum-config-manager
%{_bindir}/yum-debug-dump
%{_bindir}/yum-debug-restore
%{_bindir}/yum-groups-manager
%{_bindir}/show-installed
%{_bindir}/show-changed-rco
%{_sbindir}/yum-complete-transaction
%{_sbindir}/yumdb
%{python_sitelib}/yumutils/
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/debuginfo-install.1.*
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/repodiff.1.*
%{_mandir}/man1/reposync.1.*
%{_mandir}/man1/show-changed-rco.1.*
%{_mandir}/man1/show-installed.1.*
%{_mandir}/man1/yum-builddep.1.*
%{_mandir}/man1/yum-debug-dump.1.*
%{_mandir}/man1/yum-debug-restore.1.*
%{_mandir}/man8/yum-complete-transaction.8.*
%{_mandir}/man1/yum-groups-manager.1.*
%{_mandir}/man8/yumdb.8.*
%{_mandir}/man1/yumdownloader.1.*
%{_mandir}/man1/find-repos-of-install.1.*
%{_mandir}/man1/needs-restarting.1.*
%{_mandir}/man1/repo-graph.1.*
%{_mandir}/man1/repoclosure.1.*
%{_mandir}/man1/repomanage.1.*
%{_mandir}/man1/repotrack.1.*
%{_mandir}/man1/verifytree.1.*
%{_mandir}/man1/yum-config-manager.1.*

%files -n yum-updateonboot
%defattr(-, root, root)
%doc updateonboot/README COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/yum-updateonboot
%{_initrddir}/yum-updateonboot

%files -n yum-plugin-changelog
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/changelog.conf
%doc COPYING
%{pluginhome}/changelog.*
%{_mandir}/man1/yum-changelog.1.*
%{_mandir}/man5/yum-changelog.conf.5.*

%files -n yum-plugin-fastestmirror
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fastestmirror.conf
%{pluginhome}/fastestmirror*.*

%files -n yum-plugin-protectbase
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/protectbase.conf
%{pluginhome}/protectbase.*

%files -n yum-plugin-versionlock
%defattr(-, root, root)
%doc plugins/versionlock/README COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/versionlock.conf
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/versionlock.list
%{pluginhome}/versionlock.*
%{_mandir}/man1/yum-versionlock.1.*
%{_mandir}/man5/yum-versionlock.conf.5.*

%files -n yum-plugin-tsflags
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/tsflags.conf
%{pluginhome}/tsflags.*

%files -n yum-plugin-priorities
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/priorities.conf
%{pluginhome}/priorities.*

%if %{package_yum_updatesd}
%files -n yum-plugin-refresh-updatesd
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/refresh-updatesd.conf
%{pluginhome}/refresh-updatesd.*
%endif

%files -n yum-plugin-merge-conf
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/merge-conf.conf
%{pluginhome}/merge-conf.*

%files -n yum-plugin-upgrade-helper
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/upgrade-helper.conf
%{pluginhome}/upgrade-helper.*

%files -n yum-plugin-aliases
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/aliases.conf
%config(noreplace) %{_sysconfdir}/yum/aliases.conf
%{pluginhome}/aliases.*
%{_mandir}/man1/yum-aliases.1.*

%files -n yum-plugin-list-data
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/list-data.conf
%{pluginhome}/list-data.*
%{_mandir}/man1/yum-list-data.1.*

%files -n yum-plugin-filter-data
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/filter-data.conf
%{pluginhome}/filter-data.*
%{_mandir}/man1/yum-filter-data.1.*

%files -n yum-plugin-tmprepo
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/tmprepo.conf
%{pluginhome}/tmprepo.*

%files -n yum-plugin-verify
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/verify.conf
%{pluginhome}/verify.*
%{_mandir}/man1/yum-verify.1.*

%files -n yum-plugin-keys
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/keys.conf
%{pluginhome}/keys.*

%files -n yum-NetworkManager-dispatcher
%defattr(-, root, root)
%doc COPYING
/etc/NetworkManager/dispatcher.d/*

%files -n yum-plugin-remove-with-leaves
%defattr(-, root, root)
%doc COPYING
%{pluginhome}/remove-with-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/remove-with-leaves.conf

%files -n yum-plugin-post-transaction-actions
%defattr(-, root, root)
%doc COPYING
%{pluginhome}/post-transaction-actions.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/post-transaction-actions.conf
%doc plugins/post-transaction-actions/sample.action
# Default *.action file dropping dir.
%dir %{_sysconfdir}/yum/post-actions

%files -n yum-plugin-rpm-warm-cache
%defattr(-, root, root)
%doc COPYING
%{pluginhome}/rpm-warm-cache.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/rpm-warm-cache.conf

%files -n yum-plugin-auto-update-debug-info
%defattr(-, root, root)
%doc COPYING
%{pluginhome}/auto-update-debuginfo.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/auto-update-debuginfo.conf

%files -n yum-plugin-show-leaves
%defattr(-, root, root)
%doc COPYING
%{pluginhome}/show-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/show-leaves.conf

%files -n yum-plugin-local
%defattr(-, root, root)
%doc COPYING
%ghost %{_sysconfdir}/yum.repos.d/_local.repo
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/local.conf
%{pluginhome}/local.*

%files -n yum-plugin-fs-snapshot
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fs-snapshot.conf
%{pluginhome}/fs-snapshot.*
%{_mandir}/man1/yum-fs-snapshot.1.*
%{_mandir}/man5/yum-fs-snapshot.conf.5.*

%files -n yum-plugin-ps
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/ps.conf
%{pluginhome}/ps.*

%if %{package_puppetverify}
%files -n yum-plugin-puppetverify
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/puppetverify.conf
%{pluginhome}/puppetverify.*
%endif

%files -n yum-plugin-copr
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/copr.conf
%{pluginhome}/copr.*
%{_mandir}/man8/yum-copr.8.*

%files -n yum-plugin-ovl
%defattr(-, root, root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/ovl.conf
%{pluginhome}/ovl.*
%{_mandir}/man1/yum-ovl.1.*

%changelog
* Tue Mar 21 2017 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-42
- Add yum-plugin-copr.
- Resolves: bug#1429831

* Thu Mar 09 2017 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-41
- yum-config-manager: only select exact matches from --setopt.
- Resolves: bug#1403015
- yum-plugin-verify: set exit status to 1 in case of problems.
- Resolves: bug#1406891

* Thu Aug 04 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-40
- needs-restarting: rework reboothint logic.
- Related: bug#1192946
- needs-restarting: rebase patch for 1335587.
- Related: bug#1335587

* Fri Jul 22 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-39
- verifytree: don't fail with versioned docdirs.
- Related: bug#1296282

* Thu Jun 30 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-38
- verifytree: use local comps schema.
- Related: bug#1296282
* Tue Jun 21 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-37
- needs-restarting: add option for reboot hint.
- Resolves: bug#1192946
- needs-restarting: add option to list services.
- Resolves: bug#1335587
- reposync: add --download-metadata to the man page.
- Resolves: bug#1329649
- debuginfo-install: also respect provides when testing for installonly.
- Related: bug#1293707

* Fri May 13 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-36
- yum-config-manager: document syntax for enabling/disabling all repos.
- Resolves: bug#1245117
- verifytree: use current url of comps schema.
- Resolves: bug#1296282

* Tue Mar 01 2016 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-35
- debuginfo-install: install debuginfo only for the latest installed version of installonly package.
- Resolves: bug#1293707
- yum-config-manager: don't require enabled repos for --add-repo to work.
- Resolves: bug#1184912
- fs-snapshot: btrfsctl is obsolete, use btrfs.
- Resolves: bug#1091698
- Add libxml2-python to Requires for repo-rss.
- Resolves: bug#1297788
- Remove -v from repoquery man page.
- Resolves: bug#1285750
- yum-plugin-priorities: get all obsoletes, not just the newest.
- Resolves: bug#1269414
- yumdownloader: fix description of --archlist in the manpage.
- Resolves: bug#1264774
- yum-builddep: mention the workaround for arched srpms in the man page.
- Resolves: bug#1156057

* Mon Oct 12 2015 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-34
- ovl plugin: run at init_hook stage.
- Resolves: bug#1269395

* Fri Sep 04 2015 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-33
- ovl plugin: remove fs check and add manpage.
- Related: bug#1213602

* Tue Aug 04 2015 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-32
- ovl plugin: change copy-up strategy, execute when root fs is mounted OverlayFS, add logging.
- Related: bug#1213602

* Thu Jul 02 2015 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-31
- yum-builddep: respect --tolerant to ignore missing dependencies.
- Resolves: bug#817046

* Tue May 26 2015 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-30
- yum-config-manager: update config file specified using -c option.
- Resolves: bug#1075708
- yum-config-manager: require \* syntax to disable all repos.
- Resolves: bug#1151154
- Add plugin for overlayfs issue workaround.
- Resolves: bug#1213602

* Mon Nov 10 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-29
- reposync: fix man page formatting.
- Related: bug#1121714

* Wed Sep 24 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-28
- needs-restarting: handle RepoError gracefully.
- Resolves: bug#1107658

* Wed Sep 24 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-27
- reposync: preserve directory structure.
- Resolves: bug#1139032
- reposync: check for existing packages when using -u option.
- Resolves: bug#1140864

* Thu Sep  4 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-26
- yum-post-transaction-actions: allow colons in command part.
- Resolves: bug#1134989
- reposync: show urls for all repos when using -u option.
- Resolves: bug#1133125
- yum-config-manager: fix --save when --setopt contains wildcards.
- Resolves: bug#1129590
- post-transaction-actions: fix filename matching.
- Resolves: bug#1127782
- reposync: add missing switches to the manpage.
- Resolves: bug#1121714
- yumdownloader: print depsolving errors instead of ignoring them.
- Resolves: bug#1113391
- yumdownloader: make --destdir less of a hack.
- Resolves: bug#1104995
- needs-restarting: multiple fixes.
- Resolves: bug#1095150

* Tue Aug  5 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-25
- yumdownloader, yum-builddep: do not ignore source repos.
- Resolves: bug#1082050

* Fri Feb 14 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-24
- reposync: fix 'reposync -r nosuchrepo' behaviour.
- Resolves: bug#1060702

* Mon Jan 20 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-23
- yum-builddep: Use srpms in already enabled repos.
- Resolves: bug1024070

* Wed Jan 15 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-22
- Fix repo suffix to '-debug-rpms' in debuginfo-install.
- Resolves: bug#1052871

* Fri Jan 10 2014 Valentina Mukhamedzhanova <vmukhame@redhat.com> - 1.1.31-21
- Fix YumBaseError name error in repoquery
- Resolves: bug#1050218

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.31-20
- Mass rebuild 2013-12-27

* Fri Nov  1 2013 James Antill <james.antill@redhat.com> - 1.1.31-19
- Remove security plugin.
- Resolves: rhbz#1002491

* Mon Sep  9 2013 James Antill <james.antill@redhat.com> - 1.1.31-18
- Disable puppetverify plugin for el7. BZ 1002876.
- reposync: fix a copy-paste error. BZ 994514
- repo-rss: non-ASCII fix, sorting.
- Add --nogroups and --noplugins options to verifytree.

* Wed Jul 31 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-17
- Use new findRepos() API for yum-config-manager. BZ 971599

* Wed Jul 31 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-16
- Update to latest HEAD
- Fix pacakge => package typos
- docs: Add missing man page short descriptions
- docs: Escape dashes in command-line options
- docs: Add missing man pages for all yum-utils
- Add --show-duplicates to repoquery manpage. BZ 975565
- yum-complete-transaction: unlock yum.pid. BZ 984119
- sanitize repoquery --repofrompath. BZ 988140
- yum changelog: implicit since=all. BZ 961782
- repoquery: retry doLock() BZ 988223
- repoquery: add --installroot option. BZ 988429

* Mon Jun 24 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-15
- Update to latest HEAD
- debuginfo-install: handle YumBaseError
- fs-snapshot: "dmsetup -o" workaround.  BZ 954358, BZ 949569
- tmprepo: avoid spaces in repoid. BZ 965806
- repoquery: add cachedir locking. BZ 969776
- Fix a bug in Modified/Upgraded/Downgraded output. BZ 819502

* Thu Apr 18 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-14
- yum-utils.bash: load yum.bash first

* Wed Apr 17 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-13
- Update to latest HEAD
- versionlock add: Skip packages already locked.
- versionlock delete: Match all names, not just envra.
- Allow --old=/foo urls for repodiff.
- Don't check timestamps for repofrompath repos. BZ 880944
- Output couldn't find a pkg. for 'foo'. BZ 838158

* Tue Mar 12 2013 James Antill <james@fedoraproject.org> - 1.1.31-12
- Update to latest HEAD.
- FS snapshot tweaks for snapper support.

* Mon Mar 11 2013 James Antill <james@fedoraproject.org> - 1.1.31-11
- Update to latest HEAD.
- FS snapshot fixes, and thin provisioning support.
- search-quiet for yumdb.

* Wed Feb  6 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-10
- Update to latest HEAD
- Small fixes in documentation and error handling

* Mon Jan 14 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-9
- Update to latest HEAD.
- Added pluginhome define to get rid of hardcoded paths
- Fix yum-NetworkManager-dispatcher description, BZ 894729
- reposync should lock. BZ 880722
- Initialize exit_code correctly.  BZ 882536

* Mon Jan 14 2013 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-8
- Update to latest HEAD.

* Wed Aug  8 2012 Zdenek Pavlas <zpavlas@redhat.com> - 1.1.31-7
- Update to latest HEAD.
- Use package downloader from Yum.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 James Antill <james@fedoraproject.org> - 1.1.31-5
- Update to latest HEAD.

* Thu Jan 26 2012 James Antill <james@fedoraproject.org> - 1.1.31-4
- Update to latest HEAD.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 13 2011 Tim Lauridsen <timlau@fedoraproject.org> 
- fix traceback in auto-update-debuginfo plugin (rhbz #729982)

* Thu Aug 10 2011 Tim Lauridsen <timlau@fedoraproject.org> 
- mark as 1.1.31
- remove patches

* Thu Jul 28 2011 James Antill <james@fedoraproject.org>
- Fix for BuildTrans no return value checking, needed for mock.
- Resolves: bug#716267

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Tim Lauridsen <timlau@fedoraproject.org> 
- mark as 1.1.30 
 
* Mon Jan 3 2011 Tim Lauridsen <timlau@fedoraproject.org>
- Added yumutils python module
 
* Thu Dec 30 2010 Tim Lauridsen <timlau@fedoraproject.org>
- Added Translation support and need Requires, BuildRequires 

* Sun Nov 7 2010 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.29 

* Tue Aug  3 2010 Seth Vidal <skvidal at fedoraproject.org>
- add COPYING docs to all the plugins to make fedora(and Tim) happy. :)

* Tue Aug 3 2010 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.28 

* Sun Jun 6 2010 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.27  

* Wed Feb 10 2010 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.26  

* Wed Jan 27 2010 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.25
- add touch /etc/yum.repos.d/_local.repo to install section
- this need for for the ghost in files section of yum-plugin-local

* Sun Nov 8 2009 Tim Lauridsen <timlau@fedoraproject.org>
- remove basearchonly since all versions of yum for quite some time obsolete it
- truncate changelog to last 2 years

* Sat Nov 7 2009 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.24

* Wed Nov  4 2009 Seth Vidal <skvidal at fedoraproject.org>
- add needs-restarting

* Mon Oct 12 2009 Seth Vidal <skvidal at fedoraproject.org>
- add python compileall to all plugins so we get .pyc/.pyo files in them
- fixes https://bugzilla.redhat.com/show_bug.cgi?id=493174

* Wed Sep 2 2009 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.23

* Tue May 19 2009 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.22 

* Mon May 18 2009 Seth Vidal <skvidal at fedoraproject.org>
- add show-leaves plugin from Ville Skyttä

* Wed Mar 25 2009 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.21 

* Mon Mar 2 2009 Tim Lauridsen <timlau@fedoraproject.org>
- set yum require to 3.2.21 (the 3.2.21 in rawhide is patched to yum head, so it matches the need yum 3.2.22 code)
- Added versioned Provides: yum-<pluginname> to make rpm/yum happy.
- yum-updateonboot is not renamed and dont need Obsoletes/Conflicts/Provides

* Sun Mar 1 2009 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.20
- rename plugins from yum-name to yum-plugin-name

* Wed Feb 25 2009 Tim Lauridsen <timlau@fedoraproject.org> 
- Remove yum-kernel-module & yum-fedorakmod plugins (no obsoleting yet)
- Remove yum-skip-broken plugin leftovers

* Tue Feb  3 2009 James Antill <james@fedoraproject.org>
- add auto-update-debuginfo plugin

* Wed Dec 17 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.19

* Wed Dec 10 2008 Seth Vidal <skvidal at fedoraproject.org>
- add find-repos-of-install from James' stash of misc stuff

* Wed Oct 29 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.18

* Mon Oct 27 2008 Seth Vidal <skvidal at fedoraproject.org>
- add rpm-warm-cache plugin

* Fri Sep 19 2008 Tim Lauridsen <timlau@fedoraproject.org>
- removed skip-broken plugin

* Wed Sep 17 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.17

* Mon Sep  8 2008 Seth Vidal <skvidal at fedoraproject.org>
- add yum-remove-with-leaves plugin

* Wed Aug 27 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.16
* Wed Aug 20 2008 James Antill <james@fedoraproject.org>
- add yum-groups-manager

* Thu Aug 7 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.15
* Wed May 21 2008 Tim Lauridsen <timlau@fedoraproject.org>
- add verifytree

* Wed May 21 2008 Tim Lauridsen <timlau@fedoraproject.org>
  Make yum-fastestmirror %%files handle the fastestmirror-asyncore.py file
* Wed May 21 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.14
* Fri Apr 10 2008 James Antill <james@fedoraproject.org>
- Add keys plugin

* Fri Mar 31 2008 James Antill <james@fedoraproject.org>
- Add yum-aliases man page

* Fri Mar 21 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.13
* Fri Mar 21 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.12
* Tue Mar 18 2008 Shawn Starr <shawn.starr@rogers.com>
- Add yum-utils.1 manual page
- Rename yum-complete-transaction manual page to 8
- Move yum-complete-transaction to /usr/sbin

* Sat Mar  1 2008 James Antill <james@fedoraproject.org>
- Add verify plugin

* Wed Feb 20 2008 James Antill <james@fedoraproject.org>
- Add empty versionlock file

* Fri Feb  1 2008 James Antill <james@fedoraproject.org>
- Add filter-data plugin

* Wed Jan 30 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.11

* Sun Jan 13 2008 Seth Vidal <skvidal at fedoraproject.org>
- add repodiff

* Thu Jan 3 2008 Tim Lauridsen <timlau@fedoraproject.org>
- mark as 1.1.10

