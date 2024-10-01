import boto3
from dotenv import load_dotenv
import os
import airflow.dags.transformation as transformation

def load_youtube_data():
    csv_folder_path = transformation.transform_youtube_data()
    bucket_name = 'yt-analysis-bucket'
    s3_file_key = 'processed_data/Youtube_Data_transformation'
    upload_to_s3(csv_folder_path, bucket_name, s3_file_key)



def upload_to_s3(folder_path, bucket_name, s3_file_key):
    load_dotenv()
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region='us-east-1' 

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            local_file_path = os.path.join(folder_path, file_name)
            try:
                s3_client.upload_file(local_file_path, bucket_name, s3_file_key)
                print(f"File {local_file_path} successfully uploaded to S3 bucket.")
            except Exception as e:
                print(f"Error uploading file to S3: {e}")
            break
    else:
        print(f"No CSV file found in {folder_path}")


load_youtube_data()