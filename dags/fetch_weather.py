from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import os
import random

# -------- Konfigurasi --------
CITY = 'Jakarta'
OUTPUT_DIR = '/opt/airflow/data/'  # untuk Docker Airflow
# OUTPUT_DIR = './data/'  # kalau dijalankan lokal

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# -------- Fungsi Python --------
def generate_mock_weather():
    # Buat mock data cuaca
    mock_data = {
        "city": CITY,
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(25, 34), 2),
        "humidity": random.randint(60, 90),
        "weather": random.choice(["Clear", "Clouds", "Rain", "Thunderstorm"]),
        "wind_speed": round(random.uniform(1.0, 5.0), 2),
    }

    # Simpan ke file JSON
    filename = f"{OUTPUT_DIR}{CITY}_{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(mock_data, f, indent=2)
    print(f"Mock weather data saved to {filename}")

# -------- DAG Definition --------
with DAG(
    dag_id='mock_fetch_weather_data',
    default_args=default_args,
    description='Generate mock daily weather data for testing pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['weather', 'mock', 'data-ingestion'],
) as dag:

    task_generate_mock_weather = PythonOperator(
        task_id='generate_mock_weather',
        python_callable=generate_mock_weather
    )

    task_generate_mock_weather
