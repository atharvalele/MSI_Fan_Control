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
f = open(EC_FILE, 'r+b')

# open profile file
pf = open(PROFILE_FILE, 'r')

def write_ec(value, address):
        f.seek(address)
        # read in old value byte, ord() used so that python outputs unicode value
        old_val = ord(f.read(1))
        if old_val != value:
                print('{0}: {1} -> {2}'.format(address, old_val, value))
                f.write(bytearray([value]))
        else:
                print('{0}: {1}'.format(address, value))

for line in pf.readlines():
        if line.startswith('>'):
                address, val = line.split()[1:3]
                write_ec(int(val, 16), int(address,16))