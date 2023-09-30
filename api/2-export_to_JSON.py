import sys
import requests
import json


def get_employee_info(employee_id):
    # Retrieve employee details
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    # Retrieve TODO list for the employee
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Prepare TODO list data in JSON format
    data = {str(employee_id): []}
    for todo in todos:
        task_data = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name
        }
        data[str(employee_id)].append(task_data)

    # Export TODO list data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)

    print(f"Data exported to {filename} successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
