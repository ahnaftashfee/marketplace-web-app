"""

Initializes the sql database  ..

"""
import sqlite3

def connect_to_db():

    """
    
    Connects to the database and then executes the schema.sql script on it

    """
    try:
        with sqlite3.connect("backend/marketplace.db") as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

            with open("backend/schema.sql", "r", encoding="utf-8") as file:
                sql_script = file.read()

            conn.executescript(sql_script)
            print("Executed schema.sql successfully")

    except sqlite3.OperationalError as e:
        print("falied to open database:", e)

if (__name__) == "__main__":
    connect_to_db()
