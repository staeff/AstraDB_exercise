from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import csv

with open('GeneratedToken', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Sktip the first line
    next(reader)
    client_id, client_secret, role, token = next(reader)

# https://docs.datastax.com/en/developer/python-driver/3.25/getting_started/

cloud_config= {
        'secure_connect_bundle': 'secure-connect-nosql-db.zip'
}
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")