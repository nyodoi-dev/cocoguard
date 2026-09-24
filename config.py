import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")

connection_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "181a43f36200e4044fe400ab6ee609920892904f048c048d05c8f5813f3dc92a")

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(connection_string)
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False