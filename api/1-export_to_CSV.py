import csv
import sys
import os


def user_info(id):
    filename = str(id) + ".csv"
    if not os.path.exists(filename):
        print(f"CSV file '{filename}' does not exist.")
        return

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        tasks = list(reader)

    num_tasks = len(tasks) - 1  # Subtracting 1 to exclude the header row
    print(f"Number of tasks in CSV: {num_tasks}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <user_id>")
        return

    user_id = int(sys.argv[1])
    user_info(user_id)


if __name__ == "__main__":
    main()
