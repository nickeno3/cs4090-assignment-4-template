#test_basic.py
import pytest
import os
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from tasks import (
    load_tasks,
    save_tasks,
    filter_tasks_by_priority,
    filter_tasks_by_category,
    generate_unique_id,
    filter_tasks_by_completion,
    search_tasks,
    get_overdue_tasks,
)

# Temporary test file
TEST_FILE = "test_tasks.json"

# Sample data for tests
sample_tasks = [
    {"id": 1, "title": "Task 1", "priority": "High", "category": "Work", "completed": False},
    {"id": 2, "title": "Task 2", "priority": "Low", "category": "Personal", "completed": True},
    {"id": 3, "title": "Task 3", "priority": "High", "category": "School", "completed": False},
]

def test_save_and_load_tasks():
    save_tasks(sample_tasks, file_path=TEST_FILE)
    loaded = load_tasks(file_path=TEST_FILE)
    assert loaded == sample_tasks

def test_filter_tasks_by_priority():
    high_priority = filter_tasks_by_priority(sample_tasks, "High")
    assert len(high_priority) == 2
    assert all(task["priority"] == "High" for task in high_priority)

def test_filter_tasks_by_category():
    school = filter_tasks_by_category(sample_tasks, "School")
    assert len(school) == 1
    assert school[0]["category"] == "School"

def test_generate_unique_id():
    uid = generate_unique_id(sample_tasks)
    assert uid == 4

def test_load_tasks_file_not_found():
    result = load_tasks(file_path="nonexistent.json")
    assert result == []

def test_filter_tasks_by_completion():
    tasks = [
        {"id": 1, "completed": True},
        {"id": 2, "completed": False},
    ]
    completed = filter_tasks_by_completion(tasks, completed=True)
    assert len(completed) == 1 and completed[0]["id"] == 1

def test_search_tasks():
    tasks = [
        {"title": "Buy groceries", "description": "Milk and eggs"},
        {"title": "Study", "description": "CS4090 homework"},
    ]
    results = search_tasks(tasks, "groceries")
    assert len(results) == 1 and results[0]["title"] == "Buy groceries"

def test_get_overdue_tasks():
    today_str = datetime.now().strftime("%Y-%m-%d")
    yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    tasks = [
        {"title": "Old task", "due_date": yesterday_str, "completed": False},
        {"title": "Done task", "due_date": yesterday_str, "completed": True},
        {"title": "Future task", "due_date": today_str, "completed": False},
    ]
    overdue = get_overdue_tasks(tasks)
    assert len(overdue) == 1
    assert overdue[0]["title"] == "Old task"

def test_load_tasks_corrupted_json(tmp_path):
    # Create invalid JSON file
    bad_file = tmp_path / "bad_tasks.json"
    bad_file.write_text("{invalid json...")

    tasks = load_tasks(file_path=str(bad_file))
    assert tasks == []  # should return empty list safely

# Cleanup
def teardown_module(module):
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
