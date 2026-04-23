import pandas as pd
 
DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
 
def load_data():
    df = pd.read_parquet(DATA_URL)
 
    # Reduce size for performance
    df = df.sample(n=50000, random_state=42)
 
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["date"] = df["tpep_pickup_datetime"].dt.date
 
    return df

if __name__=="main":
    print(load_data.head)