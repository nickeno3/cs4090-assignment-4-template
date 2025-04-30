import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src")))

from pytest_bdd import scenarios, given, when, then
from tasks import filter_tasks_by_category, filter_tasks_by_priority

scenarios('../../../tests/feature/add_task.feature')

# Shared task list
task_list = []

# ---------- GIVEN STEPS ----------

@given("I have an empty task list")
def empty_task_list():
    global task_list
    task_list = []

@given('I have a task titled "Buy milk"')
def task_buy_milk():
    global task_list
    task_list = [{"title": "Buy milk", "completed": False}]

@given('I have a task titled "Take out trash"')
def task_take_out_trash():
    global task_list
    task_list = [{"title": "Take out trash", "completed": False}]

@given('I have tasks in category "Work"')
def tasks_in_work_category():
    global task_list
    task_list = [{"title": "Email client", "category": "Work"}]

@given('I have tasks with priority "High"')
def tasks_with_high_priority():
    global task_list
    task_list = [{"title": "Study", "priority": "High"}]

# ---------- WHEN STEPS ----------

@when('I add a task titled "Do homework"')
def add_task():
    global task_list
    task_list.append({"title": "Do homework"})

@when("I mark the task as complete")
def mark_complete():
    global task_list
    for task in task_list:
        task["completed"] = True

@when("I delete the task")
def delete_task():
    global task_list
    task_list = []

@when('I filter tasks by category "Work"')
def filter_by_category():
    global task_list
    task_list = filter_tasks_by_category(task_list, "Work")

@when('I filter tasks by priority "High"')
def filter_by_priority():
    global task_list
    task_list = filter_tasks_by_priority(task_list, "High")

# ---------- THEN STEPS ----------

@then('the task list should contain "Do homework"')
def verify_task_added():
    global task_list
    assert any(task["title"] == "Do homework" for task in task_list)

@then("the task should be marked as complete")
def verify_complete():
    global task_list
    assert all(task["completed"] is True for task in task_list)

@then('the task list should not contain "Take out trash"')
def verify_deleted():
    global task_list
    assert all(task["title"] != "Take out trash" for task in task_list)

@then('I should see only tasks from "Work"')
def verify_work_filtered():
    global task_list
    assert all(task["category"] == "Work" for task in task_list)

@then('I should see only tasks with "High" priority')
def verify_priority_filtered():
    global task_list
    assert all(task["priority"] == "High" for task in task_list)
