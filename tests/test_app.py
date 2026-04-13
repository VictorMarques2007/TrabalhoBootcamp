import pytest
from src.app import add_task, list_tasks, remove_task

def test_add_task():
    add_task("Estudar")
    assert "Estudar" in list_tasks()

def test_empty_task():
    with pytest.raises(ValueError):
        add_task("")

def test_remove_invalid():
    with pytest.raises(IndexError):
        remove_task(999)