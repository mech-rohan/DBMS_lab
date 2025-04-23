# db_connection.py

import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Change if using a different user
        password="#my108SQL",  # Replace with your actual MySQL password
        database="hmsproject"
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully!")
except mysql.connector.Error as e:
    print("❌ Error connecting to MySQL:", e)
