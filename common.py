#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from Utils.shell import Colors

version = '2.0.5.3'
source = '0.9'
next_source = '2.0.0.0'

prefix = '[unifiedban] '
prefix_bold  = Colors.bold + prefix + Colors.endc
prefix_fail = Colors.fail + prefix_bold
prefix_ok = Colors.ok + prefix_bold
prefix_info = Colors.info + prefix_bold

log_name = 'unifiedban_log'

supported_languages = [
	'it_IT',
	'en_US',
	'pr_PR'
]
