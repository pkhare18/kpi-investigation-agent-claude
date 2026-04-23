import pandas as pd
import os
 
DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
LOCAL_PATH = "sample_data/yellow_tripdata_2023-01.parquet"
 
def download_data():
    if not os.path.exists(LOCAL_PATH):
        print("Downloading dataset...")
        df = pd.read_parquet(DATA_URL)
        df.to_parquet(LOCAL_PATH)
        print("Saved locally!")
    else:
        print("Dataset already exists.")
 
def load_data():
    download_data()
 
    df = pd.read_parquet(LOCAL_PATH)
 
    # Reduce size
    df = df.sample(n=50000, random_state=42)
 
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["date"] = df["tpep_pickup_datetime"].dt.date
 
    return df

def compute_kpis(df):
    daily_trips = df.groupby("date").size()
 
    avg_fare = df["fare_amount"].mean()
 
    df["hour"] = df["tpep_pickup_datetime"].dt.hour
    trips_by_hour = df.groupby("hour").size()
 
    top_zones = df["PULocationID"].value_counts().head(5)
 
    return {
        "daily_trips": daily_trips,
        "avg_fare": avg_fare,
        "trips_by_hour": trips_by_hour,
        "top_zones": top_zones
    }

if __name__=="__main__":
    df=load_data()
    print(df.head())

    kpis = compute_kpis(df)
    print("Avg Fare:", kpis["avg_fare"])