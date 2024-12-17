task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires your attention."
    case "medium":
        reminder += " that should be completed soon."
    case "low":
        reminder += " that can be completed at your convenience."
    case _:
        reminder = "Invalid priority entered. Please choose high, medium, or low."

if time_bound == "yes" and "Invalid priority" not in reminder:
    reminder = reminder.replace("that", "that requires immediate attention today and")

print(f"Reminder: {reminder}")
