from cassandra.cluster import Cluster

def connect_to_cassandra(host, keyspace):
    try:
        # Connect to the Cassandra cluster
        cluster = Cluster([host])
        session = cluster.connect()

        # Check if the keyspace exists, create it if not
        keyspace_metadata = cluster.metadata.keyspaces
        if keyspace not in keyspace_metadata:
            create_keyspace_query = f"CREATE KEYSPACE {keyspace} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 2}}"
            session.execute(create_keyspace_query)

        # Use the specified keyspace
        session.set_keyspace(keyspace)

        return cluster, session
    except Exception as e:
        print(f"Error connecting to Cassandra: {e}")
        raise

def close_cassandra_connection(cluster):
    try:
        # Close the connection to Cassandra
        cluster.shutdown()
    except Exception as e:
        print(f"Error closing Cassandra connection: {e}")
        raise
