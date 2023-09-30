import sys
import requests


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

    # Calculate TODO list progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo["completed"])

    # Display employee TODO list progress
    print(
        f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo["completed"]:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
