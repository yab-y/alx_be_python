# daily_reminder.py

# Prompt the user for task information
task = input("Enter your task description: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Display reminder using match-case (Python 3.10+)
match priority:
    case "high":
        message = f"🔴 High priority task: '{task}'."
    case "medium":
        message = f"🟠 Medium priority task: '{task}'."
    case "low":
        message = f"🟢 Low priority task: '{task}'."
    case _:
        message = f"⚪ Task: '{task}' with unknown priority."

# Check if task is time-sensitive
if time_bound == "yes":
    message += " This is a time-sensitive task that requires immediate attention today!"

# Print final reminder
print("\n📌 Reminder:")
print(message)
