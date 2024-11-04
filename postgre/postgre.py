import psycopg2
from psycopg2 import OperationalError

def test_connection():
    connection = None  # Initialize the connection variable
    try:
        # Establish the connection using default PostgreSQL user 'postgres'
        connection = psycopg2.connect(
            host="localhost",         # Replace with your PostgreSQL server host
            # database="your_database", # Uncomment and replace with your database name if needed
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
