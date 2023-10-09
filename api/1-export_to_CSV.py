import csv
import sys


def export_tasks_to_csv(user_id, tasks):
    filename = f"{user_id}.csv"
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": task["username"],
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_csv.py <user_id>")
        return

    user_id = sys.argv[1]

    # Assuming tasks is a list of dictionaries containing task data
    tasks = [
        {"username": "Antonette", "completed": False,
            "title": "suscipit repellat esse quibusdam voluptatem incidunt"},
        {"username": "Antonette", "completed": True,
            "title": "distinctio vitae autem nihil ut molestias quo"},
        # ... more tasks ...
    ]

    export_tasks_to_csv(user_id, tasks)
    print(f"Data exported to {user_id}.csv")


if __name__ == "__main__":
    main()
