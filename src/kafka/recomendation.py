import json

from kafka import KafkaConsumer
from kafka import KafkaProducer



FEATURES_KAFKA_TOPIC = "Features"
RECOMENDATION_KAFKA_TOPIC = "recomendation"

consumer = KafkaConsumer(
    FEATURES_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)
producer = KafkaProducer(bootstrap_servers="localhost:29092")


print("Gonna start listening")
while True:
    for message in consumer:
        print("Ongoing recomendation..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)

        producer.send(RECOMENDATION_KAFKA_TOPIC, json.dumps(consumed_message).encode("utf-8"))

