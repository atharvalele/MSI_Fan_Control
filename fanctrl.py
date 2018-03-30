#!/usr/bin/env python

import os
import sys

# set path to Embedded Controllers i/o file
EC_FILE = '/sys/kernel/debug/ec/ec0/io'

# set path to profile file
PROFILE_FILE = 'profiles/QuietPerf.rw'

if not os.path.exists(EC_FILE):
        os.system('modprobe ec_sys write_support=1')

# open EC file in binary mode
f = open(EC_FILE, 'rb')
print(f.readlines())