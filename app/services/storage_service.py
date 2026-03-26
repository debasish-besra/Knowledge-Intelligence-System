import boto3
from botocore.exceptions import ClientError
from config import Config


class S3Storage:
    def __init__(self):
        if not Config.AWS_ACCESS_KEY or not Config.AWS_SECRET_KEY:
            raise ValueError("AWS credentials missing in .env")

        self.bucket = Config.AWS_BUCKET_NAME

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY,
        )

    def upload_file(self, file_obj, filename):
        try:
            self.s3.upload_fileobj(file_obj, self.bucket, filename)
            return True
        except ClientError as e:
            print(f"S3 Upload Error: {e}")
            return False

    def download_file(self, filename, local_path):
        try:
            self.s3.download_file(self.bucket, filename, local_path)
            return local_path
        except ClientError as e:
            print(f"S3 Download Error: {e}")
            return None

    def get_file_stream(self, filename):
        try:
            response = self.s3.get_object(Bucket=self.bucket, Key=filename)
            return response["Body"]
        except ClientError as e:
            print(f"S3 Stream Error: {e}")
            return None