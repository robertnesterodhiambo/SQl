import psycopg2
import json

def load_database():
    # Connect to the PostgreSQL test database
    connection = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="postgres", #user place your own
        password="root" #password use your own
    )
    return connection

def fetch_qep(sql_query):
    connection = load_database()
    qep_result = None
    try:
        with connection.cursor() as cursor:
            # Retrieve QEP with EXPLAIN in JSON format
            cursor.execute(f"EXPLAIN (FORMAT JSON) {sql_query}")
            qep_result = cursor.fetchone()
    finally:
        connection.close()
    
    # Return the QEP as a JSON string for easier parsing and cost extraction
    return json.dumps(qep_result[0]) if qep_result else "No QEP found"
