import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_db")

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing in .env")

        # AWS optional (for now)
        # Uncomment when S3 integration used
        # if not Config.AWS_ACCESS_KEY:
        #     raise ValueError("AWS_ACCESS_KEY missing")