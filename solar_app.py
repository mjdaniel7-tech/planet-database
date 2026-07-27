\
"""
solar_app.py

Placeholder starter file.

Note:
The full application discussed in the chat is several hundred lines long.
This file is created so you have the correct filename and can begin
building your project. You can continue filling in the functions as
planned:

- Connect to MySQL
- List all planets
- View planet details
- View a planet's moons
- Search by planet
- Search by moon
- Reports

Required package:
    pip install mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "solar_system",
}


def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Database connection failed: {e}")
        return None


def main():
    conn = get_connection()
    if not conn:
        return

    print("Solar System Database")
    print("=====================")
    print("Connection successful.")

    conn.close()


if __name__ == "__main__":
    main()
