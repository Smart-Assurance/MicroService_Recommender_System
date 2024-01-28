from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os

default_args = {
    'owner': 'said',
    'start_date': datetime(2024, 1, 28),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    dag_id='pipeline_recommender_system',
    default_args=default_args,
    description='A simple Airflow DAG for dataset preprocessing and KNN model training',
    schedule_interval='@daily',  # Set the desired schedule interval
)

# Define a function for preprocessing
def preprocess_data():
    # Call the preprocess script
    command = 'python ../Scripts/data_pre_processing.py'
    os.system(command)

# Define a function for training the KNN model
def train_knn_model():
    # Call the train_model script
    command = 'python ../Scripts/KNN_train_model.py'
    os.system(command)

# Define PythonOperators for each task
preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_knn_model',
    python_callable=train_knn_model,
    dag=dag,
)

# Set the task dependencies
preprocess_task >> train_model_task
