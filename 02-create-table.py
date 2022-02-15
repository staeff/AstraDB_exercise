#!/usr/bin/env python3
from connection import session

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS todoitems (
                        user_id         TEXT,
                        item_id         TIMEUUID,
                        title           TEXT,
                        completed       BOOLEAN,
                        PRIMARY KEY ((user_id), item_id)
                    ) WITH CLUSTERING ORDER BY (item_id ASC);
"""

print('Creating table todoitems')
session.execute(CREATE_TABLE)
