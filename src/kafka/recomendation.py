import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

import pandas as pd
import joblib

# Load the Label Encoder

label_encoder_marque_path = '../../model/label_encoder_marque.joblib'
label_encoder_marque = joblib.load(label_encoder_marque_path)
# print(label_encoder_marque.classes_)

label_encoder_model_path = '../../model/label_encoder_model.joblib'
label_encoder_model = joblib.load(label_encoder_model_path)
# print(label_encoder_model.classes_)

label_encoder_Carburant_path = '../../model/label_encoder_Carburant.joblib'
label_encoder_Carburant = joblib.load(label_encoder_Carburant_path)
# print(label_encoder_Carburant.classes_)

label_encoder_BV_path = '../../model/label_encoder_BV.joblib'
label_encoder_BV = joblib.load(label_encoder_BV_path)
# print(label_encoder_BV.classes_)

label_encoder_assurance_path = '../../model/label_encoder_assurance.joblib'
label_encoder_assurance = joblib.load(label_encoder_assurance_path)
# print(label_encoder_assurance.classes_)

# Load the Standard Scaler
scaler_path = '../../model/scaler.joblib'
scaler = joblib.load(scaler_path)

# Load the KNN model
recommendation_model_path = '../../model/recommendation_model.pkl'
recommendation_model = joblib.load(recommendation_model_path)


FEATURES_KAFKA_TOPIC = "Features"
RECOMMANDATION_KAFKA_TOPIC = "recomendation"

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
        consumed_message

        new_data = pd.DataFrame({
            'age': [consumed_message['age']],
            'marque': [consumed_message['marque']],
            'model': [consumed_message['model']],
            'Puissance fiscale': [consumed_message['Puissance fiscale']],
            'Carburant': [consumed_message['Carburant']],
            'Année': [consumed_message['Année']],
            'Boite de vitesses': [consumed_message['Boite de vitesses']],
            'etat': [consumed_message['etat']],
        })
        
        new_data['marque'] = label_encoder_marque.transform(new_data['marque'])
        new_data['model'] = label_encoder_model.transform(new_data['model'])
        new_data['Carburant'] = label_encoder_Carburant.transform(new_data['Carburant'])
        new_data['Boite de vitesses'] = label_encoder_BV.transform(new_data['Boite de vitesses'])

        new_data_scaled = scaler.transform(new_data.values)

        recommendation = recommendation_model.predict(new_data_scaled).tolist()

        # recommendation_class=label_encoder_assurance.inverse_transform(recommendation[0])
        # print("Predicted 'assurance' class:", recommendation_class)

        data = {
            "id_contract": recommendation,
            "id_client": consumed_message['id_client']
        }

        # Convert the data to a JSON string
        json_data = json.dumps(data)

        print(json_data)

        # Send the JSON string to the Kafka topic
        producer.send(RECOMMANDATION_KAFKA_TOPIC, json_data.encode('utf-8'))


