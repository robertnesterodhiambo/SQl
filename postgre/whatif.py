import json
from preprocessing import fetch_qep

def generate_modified_sql(sql_query):
    # Example modification: replace "Hash Join" with "Merge Join" in the query
    modified_sql = sql_query.replace("HASH JOIN", "MERGE JOIN")  # Adjust as needed for different what-if analyses
    modified_qep = fetch_qep(modified_sql)
    return modified_sql, modified_qep

def get_qep_cost(sql_query):
    qep = fetch_qep(sql_query)
    cost = extract_cost(qep)
    return cost

def extract_cost(qep_json):
    # Parse the JSON to find and return the cost
    try:
        qep_data = json.loads(qep_json)  # Load the JSON string into a dictionary
        # Navigate through the JSON structure to find the "Total Cost"
        if isinstance(qep_data, list) and 'Plan' in qep_data[0]:
            plan = qep_data[0]['Plan']
            if 'Total Cost' in plan:
                return plan['Total Cost']
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error extracting cost: {e}")
        return None
