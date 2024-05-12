class ToDoList
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else "◻"
                print(f"{i + 1}. [{status}] {task['task']}")
        else:
            print("Your to-do list is empty!")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            to_do_list.mark_task_as_completed(task_index)
        elif choice == "3":
            to_do_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
