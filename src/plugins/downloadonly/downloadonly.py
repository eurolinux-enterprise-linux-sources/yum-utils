#!/usr/bin/python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# by Menno Smits

from yum.plugins import PluginYumExit, TYPE_INTERACTIVE

requires_api_version = '2.1'
plugin_type = (TYPE_INTERACTIVE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    if hasattr(parser, 'plugin_option_group'):
        parser = parser.plugin_option_group

    parser.add_option('', '--downloadonly', dest='dlonly', action='store_true',
           default=False, help="don't update, just download")
    parser.add_option('', '--downloaddir', dest='dldir',
                      action='store', default=None,
                      help="specifies an alternate directory to store packages")

def postreposetup_hook(conduit):
    opts, commands = conduit.getCmdLine()
    if opts.dldir:
        repos = conduit.getRepos()
        rlist = repos.listEnabled()
        for repo in rlist:
            repo.setAttribute('pkgdir',opts.dldir)
           

def postdownload_hook(conduit):
    opts, commands = conduit.getCmdLine()
    # Don't die on errors, or we'll never see them.
    if not conduit.getErrors() and opts.dlonly:
        raise PluginYumExit('exiting because --downloadonly specified ')
