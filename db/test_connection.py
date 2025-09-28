import mysql.connector

try: 
    conn = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password="adminadmin"
    )
    if conn.is_connected():
        print("Connection successful")
    conn.close()
except mysql.connector.Error as e:
    print(f'Error: {e}')