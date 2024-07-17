# todo.py

import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file)

def add_task(task_description):
    tasks = load_tasks()
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['description']} [{status}]")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Complete task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == "2":
            try:
                task_index = int(input("Enter task number to complete: "))
                complete_task(task_index)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
