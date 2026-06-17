"""
Task Completion Tracker
Instructions

You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.

Tasks:
Define a function mark_completed_tasks that accepts a list of task names.
Iterate through the list using a for loop, and update the format like "Completed:  {task}".
Return a new list with the updated task strings.
"""

tasks_list = ["Buy groceries", "Call mom", "pay bills", "learning python"]

completed_task = []
for i in tasks_list:
    completed_task.append(f"Completed: {i}")

print(completed_task)
