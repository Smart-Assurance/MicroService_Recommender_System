import json
import time

from kafka import KafkaProducer

FEATURES_KAFKA_TOPIC = "Features"
FEATURES_LIMIT = 3

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Will generate Features (informations of user and his car) after 10 seconds")

for i in range(1, FEATURES_LIMIT):
    data = {	
        "user_id": i,
        "age": 30,
        "car_id":i,
        "marque": "dacia",
        "model": "burger",
        "Puissance fiscale":12,
        "Carburant":"Diesel",
        "Année":2017,
        "Boite de vitesses":"Automatique",
        "etat":1
    }

    producer.send(FEATURES_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(10)