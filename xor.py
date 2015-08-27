#!/usr//bin/env python

import sys

if len(sys.argv) != 3:
  print "USAGE: %s <KFFSE_XHKYOKXOHOFEDM^E_Y> <0x2a>" % (sys.argv[0])
  sys.exit(1)

flag = sys.argv[1]
key = int(sys.argv[2], 16)
decoded = []

for c in flag:
  decoded.append(chr(ord(c) ^ key))

decoded = "".join(decoded)
print "%s ^ 0x%x => %s" % (flag, key, decoded)