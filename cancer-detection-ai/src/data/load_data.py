from google.cloud import storage
import pandas as pd

def load_data(data_path):
    # Implement data loading logic
    client = storage.Client()
    bucket = client.get_bucket('your-bucket')
    blob = bucket.blob(data_path)
    df = pd.read_csv(blob.download_as_string())
    return df