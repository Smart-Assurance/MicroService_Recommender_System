# train_model.py
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_knn_model(input_file, model_file):
    # Load the preprocessed data
    df = pd.read_csv(input_file)

    # Assume the last column is the target variable, and the rest are features
    array = df.values
    X = array[:,0:8]
    y = array[:,8]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)
    # Train the KNN model

    knn_model = KNeighborsClassifier(n_neighbors=1)
    knn_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn_model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy}")

    # Save the trained model
    joblib.dump(knn_model, model_file)

if __name__ == "__main__":
    input_file = "../dataset/preprocessed_data.csv"
    model_file = "../model/recommendation_model.pkl"
    train_knn_model(input_file, model_file)
