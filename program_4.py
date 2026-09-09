# Interactive Command-Line Task Scheduler
# with Lazy Evaluation

tasks = []

while True:
    print("\n===== TASK SCHEDULER =====")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ")
        condition = input("Is the task enabled? (yes/no): ")

        # Add task to the queue
        tasks.append({
            "name": task,
            "priority": priority,
            "enabled": condition == "yes"
        })

        print("Task added successfully.")

    elif choice == "2":

        if not tasks:
            print("No tasks available.")

        else:
            print("\nRunning Tasks:")

            for task in tasks:

                # Lazy evaluation using AND and OR
                if task["enabled"] and (
                    task["priority"] == "high" or
                    task["priority"] == "low"
                ):
                    print("Executing:", task["name"])

                elif not task["enabled"]:
                    print("Skipping:", task["name"])

                else:
                    print("Invalid priority:", task["name"])

    elif choice == "3":

        if tasks:
            print("\nCurrent Task Queue:")

            for i, task in enumerate(tasks, 1):
                print(
                    i,
                    ".",
                    task["name"],
                    "| Priority:",
                    task["priority"],
                    "| Enabled:",
                    task["enabled"]
                )
        else:
            print("No tasks in queue.")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Please try again.")