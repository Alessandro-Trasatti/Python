import task_manager
from datetime import date
from sys import exit, argv

def main():
    if len(argv) <= 2:
        admissible_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        task_list = []
        manager = task_manager.Task_manager(task_list)
        while True:
            show_menu()
            user_choice: str = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8, 9): ").strip()
            if user_choice not in admissible_choices:
                print("Invalid choice; You must chose between 1, 2, 3, 4, 5, 6, 7, 8 or 9")
            else:
                if user_choice == "1":
                    try:
                        task_attributes = get_task_attributes()
                        task = task_manager.Task(*task_attributes)
                        manager.add_task(task)
                    except ValueError as e:
                        print(f"Invalid task;\n{e}")
                        continue
                elif user_choice == "2":
                    try:
                        manager.remove_task()
                    except ValueError as e:
                        print(e)
                        continue
                elif user_choice == "3":
                    manager.list_tasks()
                elif user_choice == "4":
                    manager.update_task()
                elif user_choice == "5":
                    manager.list_overdue_tasks()
                elif user_choice == "6":
                    manager.approaching_tasks()
                elif user_choice == "7":
                    manager.sort_tasks()
                elif user_choice == "8":
                    manager.show_tasks_to_do()
                else:
                    if len(argv) == 2:
                        filename = argv[1]
                        if filename.endswith(".csv") or filename.endswith(".json"):
                            manager.store_tasks_to_file(filename)
                        else:
                            exit("Invalid filename. Supported extensions are .csv and .json")
                    exit("Exiting the task manager...")
    else:
        exit(f"Error, exiting the program. Usage: main.py <filename.(csv|json)>")

def get_task_attributes():
    task_description = input("Task description: ").strip()
    task_due_date = get_date()
    task_priority = input("Task priority: ").strip()
    task_status = "To Do"
    return task_description, task_due_date, task_priority, task_status
            
    
def get_date() -> date:
    while True:
        input_date = input("Date (YYYY-MM-DD): ").strip()
        try:
            return date.fromisoformat(input_date)
        except ValueError:
            print("Invalid date format. Please try again.")
    
def show_menu() -> None:
    print("------------------------------")
    print("Task manager")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List tasks")
    print("4. Update tasks")
    print("5. List overdue tasks")
    print("6. List approaching tasks")
    print("7. Sort tasks")
    print("8. Show tasks to do")
    print("9. Exit")
    print("------------------------------")
    
if __name__ == "__main__":
    main()
    
    