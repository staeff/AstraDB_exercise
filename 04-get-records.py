#!/usr/bin/env python3
from connection import session

print('Get records from db')
output = session.execute("SELECT * FROM todoitems WHERE user_id = 'john';")
for row in output:
    print(str(row))
