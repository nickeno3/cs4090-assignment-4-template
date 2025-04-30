import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from tasks import search_tasks, get_overdue_tasks
from app_logic import mark_all_complete

# ---------- Test 1: Search Tasks ----------
def test_search_tasks_tdd():
    tasks = [
        {"title": "Buy groceries", "description": "Milk and eggs"},
        {"title": "Read book", "description": "CS4090 chapters"},
    ]
    results = search_tasks(tasks, "book")
    assert len(results) == 1
    assert results[0]["title"] == "Read book"

# ---------- Test 2: Get Overdue Tasks ----------
def test_overdue_task_tdd():
    tasks = [
        {"title": "Old task", "due_date": "2024-01-01", "completed": False},
        {"title": "Future task", "due_date": "2026-01-01", "completed": False},
    ]
    overdue = get_overdue_tasks(tasks)
    assert any(task["title"] == "Old task" for task in overdue)
    assert all(task["due_date"] < "2025-01-01" for task in overdue)

# ---------- Test 3: Mark All Complete (to be implemented by you) ----------
def test_mark_all_complete():
    from app_logic import mark_all_complete  # You will create this function
    tasks = [
        {"id": 1, "title": "A", "completed": False},
        {"id": 2, "title": "B", "completed": False},
    ]
    updated = mark_all_complete(tasks)
    assert all(task["completed"] is True for task in updated)
