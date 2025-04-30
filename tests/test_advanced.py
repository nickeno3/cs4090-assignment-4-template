import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from tasks import filter_tasks_by_priority, get_overdue_tasks
from unittest.mock import patch

sample_tasks = [
    {"title": "Task A", "priority": "Low"},
    {"title": "Task B", "priority": "Medium"},
    {"title": "Task C", "priority": "High"},
]

@pytest.mark.parametrize("priority,expected_count", [
    ("Low", 1),
    ("Medium", 1),
    ("High", 1),
    ("Urgent", 0)
])
def test_priority_param(priority, expected_count):
    result = filter_tasks_by_priority(sample_tasks, priority)
    assert len(result) == expected_count

def test_get_overdue_tasks_with_mocked_today():
    tasks = [
        {"due_date": "2024-01-01", "completed": False},
        {"due_date": "2026-01-01", "completed": False},
    ]
    # This mocks datetime.now().strftime("%Y-%m-%d") to return "2025-01-01"
    with patch("tasks.datetime") as mock_datetime:
        mock_datetime.now.return_value.strftime.return_value = "2025-01-01"
        overdue = get_overdue_tasks(tasks)
        assert len(overdue) == 1
        assert overdue[0]["due_date"] == "2024-01-01"
