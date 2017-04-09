#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()
    line = re.sub('[!?@#$,;:\/\.\-\]\[\_\(\)\'\"\&\*]', ' ', line)
    words = line.split()
    for word in words:
        if len(word) > 2:
          print '%s\t%s' % (word.lower(), 1)
