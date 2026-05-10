from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

# Load environment variables from creds.env
load_dotenv(dotenv_path="creds.env")

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        if conn.is_connected():
            print("Connected to MySQL!")
            return conn
    except Error as e:
        print(f"Connection error: {e}")
        return None