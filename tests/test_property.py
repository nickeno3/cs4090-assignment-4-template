import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import tempfile
import pytest
from hypothesis import given
from hypothesis.strategies import text, lists, sampled_from, dates, booleans
from tasks import filter_tasks_by_category, filter_tasks_by_priority, save_tasks, load_tasks

# Sample task template
def make_task(title="Task", category="Work", priority="Low", completed=False, due_date="2025-01-01"):
    return {
        "title": title,
        "category": category,
        "priority": priority,
        "completed": completed,
        "due_date": due_date,
    }

# ---------- 1. Filtering by category should never return tasks outside that category ----------
@given(
    category=sampled_from(["Work", "Personal", "School", "Other"]),
    titles=lists(text(min_size=1), min_size=1, max_size=5)
)
def test_filter_tasks_by_category_property(category, titles):
    tasks = [make_task(title=t, category=category) for t in titles]
    result = filter_tasks_by_category(tasks, category)
    assert all(task["category"] == category for task in result)

# ---------- 2. Filtering by priority should never return tasks outside that priority ----------
@given(
    priority=sampled_from(["Low", "Medium", "High"]),
    titles=lists(text(min_size=1), min_size=1, max_size=5)
)
def test_filter_tasks_by_priority_property(priority, titles):
    tasks = [make_task(title=t, priority=priority) for t in titles]
    result = filter_tasks_by_priority(tasks, priority)
    assert all(task["priority"] == priority for task in result)

# ---------- 3. Saved tasks should load back unchanged ----------

@given(
    titles=lists(text(min_size=1), min_size=1, max_size=5)
)
def test_save_and_load_tasks_roundtrip(titles):
    tasks = [make_task(title=t) for t in titles]
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as tmpfile:
        save_tasks(tasks, file_path=tmpfile.name)
        tmpfile.flush()
        loaded = load_tasks(file_path=tmpfile.name)
    assert loaded == tasks
# ---------- 4. Filtering an empty list always returns empty ----------
@given(category=sampled_from(["Work", "Personal"]))
def test_empty_list_filter_category(category):
    assert filter_tasks_by_category([], category) == []

@given(priority=sampled_from(["Low", "Medium", "High"]))
def test_empty_list_filter_priority(priority):
    assert filter_tasks_by_priority([], priority) == []
