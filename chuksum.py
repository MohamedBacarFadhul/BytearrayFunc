#!/usr/bin/python3
def calc_checksum(s):
    sum = 0
    for c in s:
        sum += ord(c)
    sum = -(sum % 256)
    return '%2X' % (sum & 0xFF)

print (calc_checksum('678888'))
