import pytest
from models import TaskList

def setup_function():
    global task_list
    task_list = TaskList()

def test_add_task():
    task_list.add_task("Task1", "Description1")
    assert "Task1" in task_list.tasks
    assert "Description1" == task_list.tasks["Task1"].description

def test_complete_task():
    task_list.add_task("Task1", "Description1")
    task_list.complete_task("Task1")
    assert task_list.tasks["Task1"].is_completed

def test_remove_task():
    task_list.add_task("Task1", "Description1")
    task_list.remove_task("Task1")
    assert "Task1" not in task_list.tasks

def test_display_tasks(capsys):
    task_list.add_task
