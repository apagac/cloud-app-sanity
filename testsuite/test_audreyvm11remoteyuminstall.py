#!/usr/bin/env python2
#   Author(s): Milan Falesnik <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2012 Red Hat, Inc. All rights reserved.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import common
import pytest

def test_install_packages_remote(audreyvars, system_uuid):
    packages = audreyvars.get("YUM_REMOTE_INSTALL", "").strip()
    server = audreyvars["KATELLO_HOST"]
    login = audreyvars.get("KATELLO_USER", "admin")
    password = audreyvars.get("KATELLO_PASS", "admin")
    if packages != "":
        packages = packages.split(" ")
    else:
        pytest.skip(msg="No packages marked for remote install")
    common.install_yum_packages_remote(server, system_uuid, login, password, packages)