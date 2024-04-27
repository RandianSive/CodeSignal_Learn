# Daily office activities
office_tasks = ["cleaning", "maintenance", "stationery_stock_check", "security_check"]

# TODO: Write a try-except block that attempts to remove the 'coffee_making' task from office_tasks
try:
    office_tasks.remove("coffee_making")
# TODO: If the task doesn't exist in the list, print a suitable message
except ValueError:
    print("There is no such task in the list!")
# TODO: Regardless of whether the task is on the list, print the message "Regardless, please ensure all tasks are attended daily."
finally:
    print("Regardless, please ensure all tasks are attended daily.")