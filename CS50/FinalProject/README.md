# Task Manager with Productivity Insights
## Project overview:
This project combines a task manager with the ability to
gather and display external data via APIs to enhance
productivity. In addition to managing tasks with priorities,
deadlines, and statuses, it integrates productivity-related data
from APIs to provide users with helpful information
(like weather, time zone data, or news).

### Key features:
1.	Task Management (Core Features):
	-	Task Creation: Users can add tasks with a description, due date, and priority level.
	-	Prioritization: Sort and filter tasks based on urgency, deadlines, or completion status.
	-	File Persistence: Save tasks in a CSV/JSON file so that tasks persist between sessions.
2.	API Integration (Productivity Insights):
	-	Weather Insights: Integrate a weather API (e.g., OpenWeatherMap) to show the current weather for a user’s location. This can help users plan outdoor tasks.
	-	Time Zone and World Clock: Use a time zone API (e.g., TimeZoneDB) to display current time and track deadlines across time zones for remote teams.
	-	News Brief: Fetch daily productivity tips or relevant news (using a news API like NewsAPI) to keep the user informed of trends or topics related to their tasks.
3.	Additional Features:
	-	Motivational Quotes API: Display random motivational quotes from an API each time the user opens the app to encourage productivity.
	-	Task Analytics: Provide insights into user productivity based on completed tasks, overdue tasks, etc., and possibly relate this to external factors (e.g., weather, energy levels).
4.	User Interface:
	-	Command-Line Interface (CLI) with options to add, delete, complete, and display tasks.
	-	Optionally, you could build a simple GUI later (e.g., using Tkinter) to display tasks, weather, time, and news side by side.

### Example workflow:
1.	Add a Task:
	-	Users can create a task by providing a description, due date, and priority level (e.g., “Write report by Friday” with high priority).
2.	Get Daily Insights:
	-	Each time the user opens the task manager, they receive a productivity insight (e.g., “Current weather: 20°C, Cloudy”, “Your time: 9:00 AM”, and a random motivational quote).
3.	View and Manage Tasks:
	-	Users can view their task list, filtered by due date or priority, and see the current weather and time zone on the same page.
4.	Complete Tasks and Get Analytics:
	-	As users mark tasks complete, they get analytics on their productivity (e.g., “You completed 3 tasks this week”, “You have 2 overdue tasks”).

### Suggested classes:
1.	Task: Represents a single task.
	-	Attributes: description, due date, priority, status.
	-	Methods: mark_complete(), update_task(), etc.
2.	TaskManager: Manages a collection of tasks.
	-	Attributes: list of tasks.
	-	Methods: add_task(), remove_task(), sort_tasks(), save_to_file(), load_from_file().
3.	APIManager: Handles API requests (weather, news, time zone).
	-	Attributes: API keys, base URLs.
	-	Methods: fetch_weather(), fetch_time_zone(), fetch_news(), fetch_quote().

### Planning
#### Week 1: Project Setup & Basic Task Management (OOP Focus)

Objectives:

1.	Set up your project environment.
2.	Create the core class structure for tasks and task management.
3.	Implement basic task creation, listing, and completion functionalities.

Tasks:

- Set up a project folder, create task_manager.py.
- Create a Task class:
- Attributes: description, due_date, priority, and status.
- Methods: mark_complete(), update_task().
- Create a TaskManager class:
- Attributes: List of tasks.
- Methods: add_task(), remove_task(), list_tasks().
- Implement a simple command-line interface (CLI) for adding and listing tasks.

Deliverables:

- A basic working task manager where users can create tasks, view them, and mark them as completed.

#### Week 2: Refining and Extending the Task Manager

1.	Task Filtering and Sorting:
-	Implement functions to filter tasks by status (e.g., view only “To Do” tasks).
-	Implement a function to sort tasks by due date or priority.
2.	Editing a Task:
-	Allow users to edit the details of an existing task (e.g., change description, due date, or priority).
3.	Task Deadline Reminders:
-	Add functionality to check for tasks that are overdue or approaching their due date.
4.	Persisting Tasks:
-	Store the tasks in a file (e.g., JSON, CSV) so that the task list persists between program runs.

## Structure
TO BE DONE
