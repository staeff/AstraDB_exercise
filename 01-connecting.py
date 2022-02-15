#!/usr/bin/env python3
from connection import session

print("Connecting to astradb")
output = session.execute("SELECT * FROM system.local")
row = output.one()
print(f"You are now connected to cluster {row.cluster_name} at {row.data_center}")
