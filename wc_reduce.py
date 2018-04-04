#!/usr/bin/env python
import sys

current_word = None
previous_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    current_word, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue

    if previous_word == current_word:
        current_count += count
    else:
        if previous_word:
            print('%s\t%s' % (previous_word, current_count))
        current_count = count
        previous_word = current_word

if previous_word == current_word:
    print('%s\t%s' % (previous_word, current_count))
