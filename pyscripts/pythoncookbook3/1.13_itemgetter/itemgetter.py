#!/usr/bin/env python

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

row_by_fname = sorted(rows, key=itemgetter('fname'))
row_by_uid = sorted(rows, key=itemgetter('uid'))

print(row_by_fname)
print(row_by_uid)

row_by_name = sorted(rows, key=lambda s: (s['fname'], s['lname']))
print(row_by_name)