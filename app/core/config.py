import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Setting(BaseSettings):
    kafka_url: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")


settings = Setting()
