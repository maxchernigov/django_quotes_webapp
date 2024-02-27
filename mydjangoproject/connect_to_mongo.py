import configparser
from pathlib import Path

import certifi
from mongoengine import connect

ca = certifi.where()

config = configparser.ConfigParser()
config.read(Path(__file__).resolve().parent / "config.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

connect(
    host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""",
    tls=True,
    tlsCAFile=ca,
)