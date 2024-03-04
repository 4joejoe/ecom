import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

database = psycopg2.connect(
    host=os.environ.get("HOST"),
    user=os.environ.get("USER"),
    password=os.environ.get("PASSWORD"),
)
database.set_session(autocommit=True)

try:
    db_crusor = database.cursor()
    print("Connected to the database successfully!")
except:
    print("Failed to connect to the database!")


try:
    db_crusor.execute("CREATE DATABASE crm_database")
    print("Database created successfully!")
except:
    print("Failed to create the database!")
finally:
    print("Closing the connection to the database...")
    database.close()
    db_crusor.close()
    print("Connection closed successfully!")
