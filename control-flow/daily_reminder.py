# daily_reminder.py

# Prompt for exact expected inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        message = f"High priority task: '{task}'."
    case "medium":
        message = f"Medium priority task: '{task}'."
    case "low":
        message = f"Low priority task: '{task}'."
    case _:
        message = f"Task: '{task}' with unknown priority."

# Add time-sensitive note if needed
if time_bound == "yes":
    message += " This is a time-sensitive task that requires immediate attention today!"

# Final output
print("Reminder:\n")
print(message)


