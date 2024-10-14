from datetime import date, timedelta
from sys import argv
from csv import DictWriter
from json import dump

possible_priorities = ["Low", "Medium", "High"]
possible_status = ["To Do", "Completed"]

class Task():
    def __init__(self, description: str, due_date: date, priority: str = "Medium", status: str = "To Do") -> None:
        self.description = description
        self.due_date = due_date 
        self.priority = priority
        self.status = status
        
    def __str__(self) -> str:
        return f"Description: {self.description};\nDue date: {self.due_date};\nPriority: {self.priority};\nStatus: {self.status};"   

    def __eq__(self, task) -> bool:
        if not isinstance(task, Task):
            return False
        else:
            same_description = (self.description == task.description)
            same_due_date = (self.due_date == task.due_date)
            same_priority = (self.priority == task.priority)
            same_status = (self.status == task.status)
            return same_description and same_due_date and same_priority and same_status
        
    def mark_complete(self) -> None:
        '''Sets the status of the task to completed.'''
        self.status = "Completed"
        
        
    # Getters
    @property
    def description(self):
        return self._description
    @property
    def due_date(self):
        return self._due_date
    @property
    def priority(self):
        return self._priority
    @property
    def status(self):
        return self._status
    
    # Setters
    @description.setter
    def description(self, description: str):
        if not description:
            raise ValueError("Task description shouldn't be empty.")
        if not isinstance(description, str):
            raise ValueError(f"Task descritption should be a string, but got {description}, which is of type {type(description)}.")
        self._description = description
        
    @due_date.setter
    def due_date(self, due_date: date):
        if not due_date: # To be removed when made optional
            raise ValueError("Task due date shouldn't be empty.") 
        if not isinstance(due_date, date):
            raise ValueError(f"Task due date should be a date, but got {due_date}, which is of type {type(due_date)}.")
        if date.today() > due_date:
            raise ValueError(f"The due date should be in the future, but got {due_date}.")
        self._due_date = due_date
        
    @priority.setter
    def priority(self, priority: str):
        if not priority: # To be removed when made optional
            raise ValueError("Task priority shouldn't be empty.")
        if not isinstance(priority, str):
            raise ValueError(f"Priority should be a string, but got {priority}, which is of type {type(priority)}.")
        if priority.lower() not in map(str.lower, possible_priorities):
            raise ValueError(f"Priority should be 'Low', 'Medium' or 'High', but got {priority}.")
        self._priority = priority.title()
        
    @status.setter
    def status(self, status: str):
        if not status:
            raise ValueError("Task status shouldn't be empty.")
        if not isinstance(status, str):
            raise ValueError(f"Task status should be a string, but got {status}, which is of type {type(status)}.")
        if status.lower() not in map(str.lower, possible_status):
            raise ValueError(f"Task status should be either 'To Do' or 'Completed', but got {status}.")
        self._status = status.title()
        
class Task_manager():
    def __init__(self, tasks_list: list):
        self.tasks_list = tasks_list
        
    def add_task(self, task: Task) -> None:
        """Adds a task to the manager's list of tasks

        Args:
            task (Task): The task to be added to the list

        Raises:
            ValueError: Triggered in case task is not an instance of Task()

        """
        if not isinstance(task, Task):
            raise ValueError(f"The task should be of type Task, but got {task}, which is of type {type(task)}.")
        if any(existing_task.description == task.description for existing_task in self.tasks_list):
            print(f"A task with the description '{task.description}' already exists.")
        self.tasks_list.append(task)
        
    def remove_task(self) -> None:
        """Removes a task from the manager's list of task if therweby present.

        Raises:
            ValueError: If an invalid task is chosen
        """
        self.list_tasks()
        try:
            index = int(input("Enter the index of the task to remove: ")) - 1
            if index < 0 or index >= len(self.tasks_list):
                raise ValueError("Invalid index")
            self.tasks_list.remove(self.tasks_list[index]) 
        except ValueError:
            print("Invalid input; please enter a number.")
        
    def list_tasks(self) -> None:
        """Prints all the tasks in a manager by enumerating them.
        """
        if self.tasks_list:
            for i, task in enumerate(self.tasks_list, start=1):
                print(f"Task {i}:\n{task}")
        else:
            print("There are no tasks yet!")
            
    def update_task(self) -> None:
        """Updates a task asking the user what should be updated
        """
        if not self.tasks_list:
            print("There are no tasks yet!")
        else:
            print("Here is a list of the existing tasks:")
            self.list_tasks()
            user_ans = self.get_index_to_change()
            task = self.tasks_list[user_ans - 1]
            while True:
                user_ans = input("Do you want to update the description? ").lower().strip()
                if user_ans not in ["yes", "no"]:
                    print(f"Invalid input; please input yes or no.")
                    continue
                if user_ans == "yes":
                    task.description = input("New task description: ")
                break
            while True:
                user_ans = input("Do you want to update the due date? ").lower().strip()
                if user_ans not in ["yes", "no"]:
                    print(f"Invalid input; please input yes or no.")
                    continue
                if user_ans == "yes":
                    while True:
                        try:
                            task.due_date = date.fromisoformat(input("New task due date (YYYY-MM-DD): ").strip())
                            break
                        except ValueError:
                            print("Invalid date. Please try again.")
                            continue
                break
            while True:
                user_ans = input("Do you want to update the status? ").lower().strip()
                if user_ans not in ["yes", "no"]:
                    print(f"Invalid input; please input yes or no.")
                    continue
                if user_ans == "yes":
                    if task.status == "to do":
                        task.mark_complete()
                    else:
                        task.status = "to do"
                break
    def list_overdue_tasks(self) -> None:
        """Prints a list of the overdue tasks
        """
        overdue_tasks = [task for task in self.tasks_list if task.due_date < date.today()]
        if not overdue_tasks:
            print("Good job! No overdue tasks")
        else:
            print("Here is a list of your overdue tasks.\n")
            for task in overdue_tasks:
                print(task, "\n")
                
    def approaching_tasks(self) -> None:
        """Prints the tasks within three days and within 7 days
        """
        tasks_due_within_next_three_days = [task for task in self.tasks_list if task.due_date - date.today() <= timedelta(days = 3)]
        print("\n-------- Here is a list of the tasks coming in the next three days---------\n")
        for task in tasks_due_within_next_three_days:
            print(task, "\n")
        print("\n-------- Here is a list of the tasks coming in the next week---------\n")
        tasks_due_within_next_week = [task for task in self.tasks_list if task.due_date - date.today() <= timedelta(days = 7)]
        for task in tasks_due_within_next_week:
            print(task, "\n")
        

    def get_index_to_change(self) -> int:
        """Gets from user the index of the task to be changed. Used in update_task() method.

        Returns:
            int: The index of the task to be changed
        """
        while True:
            try:
                user_ans = int(input("Which task do you want to update? ").strip())
            except ValueError:
                print("Invalid input; please try again.")
                continue
            self.list_tasks()
            admissible_answers = [i + 1 for i in range(len(self.tasks_list))]
            if user_ans not in admissible_answers:
                print(f"Invalid choice. Please choose a task between 1 and {admissible_answers[-1]}")
                continue
            return user_ans                       
                
                
    def sort_tasks(self) -> None:
        """Sorts the manager list of tasks either by dur_date, or by priority, depending on the user's choice.
        """
        sorting_mode = Task_manager.get_sorting_mode()
        if sorting_mode == 1:
            self.tasks_list = sorted(self.tasks_list, key=lambda x: x.due_date)
        else:
            self.sort_by_priority()
            
    def show_tasks_to_do(self) -> None:
        """Prints the tasks whose status is 'To Do'.
        """
        to_do_tasks = [task for task in self.tasks_list if task.status.lower() == "to do"]
        print("\nTASKS TO BE DONE:\n")
        for task in to_do_tasks:
            print(task, "\n")
            
    def sort_by_priority(self) -> None:
        """Sorts the manager's task list by priority. Used in sort_tasks() method.
        """
        high_priority_tasks = [task for task in self.tasks_list if task.priority.lower() == "high"]
        medium_priority_tasks = [task for task in self.tasks_list if task.priority.lower() == "medium"]
        low_priority_tasks = [task for task in self.tasks_list if task.priority.lower() == "low"]
        self.tasks_list = high_priority_tasks + medium_priority_tasks + low_priority_tasks
        
    def store_tasks_to_file(self, filename) -> None:
        """ Saves the manager's task list to a file named 'filename' either in .json or in .csv format.
            Only called if len(sys.argv) == 2 and if sys.argv[1] is either a .json or a .csv file.
            These checks are done in the main() function

        Args:
            filename (_type_): The name of the file passed by the user.
        """
        with open(filename, "w") as file:
            if filename.endswith(".csv"):
                    headers = ["Description", "Due date", "Priority", "Status"]
                    writer = DictWriter(file, fieldnames=headers)
                    writer.writeheader()
                    for task in self.tasks_list:
                        writer.writerow({"Description": task.description, "Due date": task.due_date.isoformat(), "Priority": task.priority, "Status": task.status}) 
            
            else: # It means that it is automatically a .json file
                task_list_of_dicts = [{"Description": task.description, "Due date": task.due_date.isoformat(), "Priority": task.priority, "Status": task.status} for task in self.tasks_list]
                dump(task_list_of_dicts, file, indent=4)
        
    
    @staticmethod
    def get_sorting_mode() -> str:
        """Gets the soring mode from user.

        Returns:
            str: A number (in string format) corresponding to the sorting mode;
        """
        while True:
            print("Available sorting modes:\n1. By due_date; 2. By descending priority")
            sorting_mode = input("Sorting mode:")
            if sorting_mode not in ["1", "2"]:
                print("Invalid sorting mode. Please insert either 1 or 2.")
                continue
            return sorting_mode
        
    
    # Getters
    @property
    def tasks_list(self):
        return self._tasks_list
    
    # Setters
    @tasks_list.setter
    def tasks_list(self, tasks_list: list):
        if not isinstance(tasks_list, list):
            raise ValueError(f"Task list should be a list, but got {tasks_list}, which is of type {type(tasks_list)}.")
        self._tasks_list = tasks_list