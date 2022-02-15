#!/usr/bin/env python3
import atexit
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import csv

with open('GeneratedToken', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Sktip the first line
    next(reader)
    client_id, client_secret, role, token = next(reader)

# This is the Zip file you downloaded
SECURE_CONNECT_BUNDLE = 'secure-connect-my-first-serverless-database.zip'
# This is the "Client Id" value you obtained earlier
USERNAME = client_id
# This is the "Client Secret" value you obtained earlier
PASSWORD = client_secret
# This is the keyspace name
KEYSPACE = "todos"


secure_connect_bundle = SECURE_CONNECT_BUNDLE
path_to_creds = ''
cluster = Cluster(
    cloud={
        'secure_connect_bundle': SECURE_CONNECT_BUNDLE
    },
    auth_provider=PlainTextAuthProvider(USERNAME, PASSWORD)
)
session = cluster.connect(KEYSPACE)


@atexit.register
def shutdown_driver():
    cluster.shutdown()
    session.shutdown()
