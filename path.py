#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

base = 'UnifiedBan/Bot'

dataset = base+'/Dataset'
dataset_phishing = dataset+'/phishing/phishing.database.txt'
dataset_spamlogics = dataset+'/spamlogics/'
dataset_spamlogics_images = dataset_spamlogics+'images/'

pid = base+'/unifiedban.pid'

log = base+'/status.log'
logs = base+'/Logs'
log_backup = base+'/Logs/%s__status.log'
