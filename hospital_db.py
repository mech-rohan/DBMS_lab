# hospital_db.py

import mysql.connector
from db_connection import conn, cursor  # Ensure db_connection.py handles database connection

# Function to add a new patient to the database
def add_patient(name, age, gender, disease):
    try:
        sql = "INSERT INTO patients (name, age, gender, disease) VALUES (%s, %s, %s, %s)"
        values = (name, age, gender, disease)
        cursor.execute(sql, values)
        conn.commit()
        print(f"✅ Patient '{name}' added successfully!")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

# Function to delete a patient from the database
def delete_patient(name):
    try:
        sql = "DELETE FROM patients WHERE name = %s"
        cursor.execute(sql, (name,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✅ Patient '{name}' deleted successfully!")
        else:
            print(f"⚠️ No patient found with the name '{name}'.")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

# Function to fetch all patients
def get_patients():
    try:
        cursor.execute("SELECT * FROM patients")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return []

# Testing functions (Run this file independently to test)
if __name__ == "__main__":
    add_patient("Amit Sharma", 25, "Male", "Fever")
    print(get_patients())
    delete_patient("Amit Sharma")
    print(get_patients())
