Feature: To-Do Task Management

  Scenario: Add a new task
    Given I have an empty task list
    When I add a task titled "Do homework"
    Then the task list should contain "Do homework"

  Scenario: Mark a task as complete
    Given I have a task titled "Buy milk"
    When I mark the task as complete
    Then the task should be marked as complete

  Scenario: Delete a task
    Given I have a task titled "Take out trash"
    When I delete the task
    Then the task list should not contain "Take out trash"

  Scenario: Filter by category
    Given I have tasks in category "Work"
    When I filter tasks by category "Work"
    Then I should see only tasks from "Work"

  Scenario: Filter by priority
    Given I have tasks with priority "High"
    When I filter tasks by priority "High"
    Then I should see only tasks with "High" priority
