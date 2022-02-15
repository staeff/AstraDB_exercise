#!/usr/bin/env python3
from connection import session

print('Remove a table')
session.execute("TRUNCATE TABLE todoitems;")
