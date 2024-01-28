# preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import joblib

def preprocess_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    columns_to_remove = ['user_id', 'car_id','price']
    df = df.drop(columns_to_remove, axis=1)
    df.drop(df[df['Puissance fiscale'] == 0].index, inplace=True)

    #label-encoder
    label_encoder_marque = preprocessing.LabelEncoder()
    df['marque']= label_encoder_marque.fit_transform(df['marque'])
    label_encoder_marque_path = '../model/label_encoder_marque.joblib'
    joblib.dump(label_encoder_marque, label_encoder_marque_path)

    label_encoder_model = preprocessing.LabelEncoder()
    df['model']= label_encoder_model.fit_transform(df['model'])
    label_encoder_model_path = '../model/label_encoder_model.joblib'
    joblib.dump(label_encoder_model, label_encoder_model_path)

    label_encoder_Carburant = preprocessing.LabelEncoder()
    df['Carburant']= label_encoder_Carburant.fit_transform(df['Carburant'])
    label_encoder_Carburant_path = '../model/label_encoder_Carburant.joblib'
    joblib.dump(label_encoder_Carburant, label_encoder_Carburant_path)

    label_encoder_BV = preprocessing.LabelEncoder()
    df['Boite de vitesses']= label_encoder_BV.fit_transform(df['Boite de vitesses'])
    label_encoder_BV_path = '../model/label_encoder_BV.joblib'
    joblib.dump(label_encoder_BV, label_encoder_BV_path)

    label_encoder_assurance = preprocessing.LabelEncoder()
    df['assurance']= label_encoder_assurance.fit_transform(df['assurance'])
    label_encoder_assurance_path = '../model/label_encoder_assurance.joblib'
    joblib.dump(label_encoder_assurance, label_encoder_assurance_path)

    # Perform preprocessing (example: scaling)

    array = df.values
    X = array[:,0:8]
    y = array[:,8]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    scaler_path = '../model/scaler.joblib'
    joblib.dump(scaler, scaler_path)

    # Save the preprocessed data
    df_scaled.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "../dataset/latest_global_cars.csv"
    output_file = "../dataset/preprocessed_data.csv"
    preprocess_data(input_file, output_file)
