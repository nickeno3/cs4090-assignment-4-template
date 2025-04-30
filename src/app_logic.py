def mark_all_complete(tasks):
    for task in tasks:
        task["completed"] = True
    return tasks
