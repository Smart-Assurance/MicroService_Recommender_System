import json

from kafka import KafkaConsumer
from kafka import KafkaProducer



FEATURES_KAFKA_TOPIC = "Features"
RECOMMANDATION_KAFKA_TOPIC = "recommandation"

consumer = KafkaConsumer(
    FEATURES_KAFKA_TOPIC, 
    bootstrap_servers="localhost:9092"
)

producer = KafkaProducer(bootstrap_servers="localhost:9092")


print("Gonna start listening")
while True:
    for message in consumer:
        print("Ongoing recomendation..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        # featching
        #   
        #
        # producer.send(RECOMENDATION_KAFKA_TOPIC, json.dumps(consumed_message).encode("utf-8"))
        
        # Your data
        data = {
            "id_contract": "456",
            "id_client": "65b242ee78bbaf1d76b76104"
        }

        # Convert the data to a JSON string
        json_data = json.dumps(data)

        # Send the JSON string to the Kafka topic
        producer.send(RECOMMANDATION_KAFKA_TOPIC, json_data.encode('utf-8'))
