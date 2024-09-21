# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt the user for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user to check if the task is time-sensitive
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide customized reminders based on priority and time sensitivity using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to complete it soon."
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that needs to be done by the end of the day."
        else:
            reminder += ". You can manage this task at a moderate pace."
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += ", but still time-bound. Try to complete it today."
        else:
            reminder += ". Consider completing it when you have free time."

    case _:
        reminder = "Invalid priority entered. Please enter high, medium, or low."

# Print the customized reminder
print(f"\nReminder: {reminder}")
