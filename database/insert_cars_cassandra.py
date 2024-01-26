from cassandra_connection import connect_to_cassandra, close_cassandra_connection

def insert_car(session, car_id, marque, model, Puissance_fiscale, Carburant, Boite_de_vitesses, etat):
    try:
        # Use parameterized query to prevent SQL injection
        insert_query = "INSERT INTO cars (car_id,marque, model, Puissance_fiscale,Carburant,Boite_de_vitesses,etat) VALUES (?, ?, ?, ?, ?, ?, ?)"
        session.execute(insert_query, (car_id, marque, model, Puissance_fiscale, Carburant, Boite_de_vitesses, etat))
    except Exception as e:
        print(f"Error inserting car: {e}")
        raise

def display_cars(session):
    try:
        # Query data from the 'cars' table
        select_query = "SELECT * FROM cars"
        result = session.execute(select_query)

        # Print the results
        print("Cars in the 'cars' table:")
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error displaying cars: {e}")
        raise

if __name__ == "__main__":
    # Replace these values with your Cassandra host, keyspace, and car details
    cassandra_host = '0.0.0.0'
    keyspace_name = 'recommendation_dataset'

    car_id = 1
    marque = "bmw"
    model = "Serie"
    Puissance_fiscale = 12
    Carburant = "Diesel"
    Boite_de_vitesses = "Automatique"
    etat = 1

    # Connect to Cassandra
    cluster, session = connect_to_cassandra(cassandra_host, keyspace_name)

    # Insert a car
    insert_car(session, car_id, marque, model, Puissance_fiscale, Carburant, Boite_de_vitesses, etat)

    # Display cars
    display_cars(session)
    
    # Close the connection
    close_cassandra_connection(cluster)
