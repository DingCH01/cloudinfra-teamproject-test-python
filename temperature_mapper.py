#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    if ((temperature != 9999) and line[92] != 0 and line[92] != 1 and line[92] != 4 and line[92] != 5 and line[92] != 9):
        print('%s\t%d' % (line[15:23], int(line[87:92])))
        
        
