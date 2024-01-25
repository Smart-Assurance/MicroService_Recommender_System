# get_cars.py
from mongodb_connection import get_database

def get_cars():
    # Get the database
    db = get_database()

    # Specify the collection name
    collection_name = "vehicules"  # Replace with your actual collection name
    collection = db[collection_name]

    # Retrieve all cars from the collection
    cars = list(collection.find())

    # Print or process the retrieved car data
    for car in cars:
        print(car)

get_cars()