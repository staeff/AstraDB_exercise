#!/usr/bin/env python3
from connection import session


print('Update a record')
session.execute(
    "UPDATE todoitems SET completed = true WHERE user_id = 'john' AND item_id = 22222222-5cff-11ec-be16-1fedb0dfd057;")
output = session.execute(
    "SELECT toTimestamp(item_id), completed, title FROM todoitems WHERE user_id = 'john';")
for row in output:
    print(row)
