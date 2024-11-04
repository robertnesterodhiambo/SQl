import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        # Establish the connection using default PostgreSQL user 'postgres'
        connection = psycopg2.connect(
            host="localhost",         # Replace with your PostgreSQL server host
          #  database="your_database", # Replace with your database name
            user="postgres",          # Default PostgreSQL user
            password="root"           # Replace with the correct password
        )

        # If connection is successful, print a success message
        print("Connection to PostgreSQL database successful")
        return connection

    except OperationalError as e:
        # If there’s an error, print it
        print(f"The error '{e}' occurred")
        return None

    finally:
        # Close the connection if it was opened
        if connection:
            connection.close()
            print("PostgreSQL connection closed")

# Call the function to test the connection
test_connection()
