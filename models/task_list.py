from typing import Dict, List
from .task import Task


class TaskList:
    def __init__(self) -> None:
        self.tasks: Dict[str, Task] = {}

    def add_task(self, title: str, description: str) -> None:
        task = Task(title, description)
        self.tasks[title] = task

    def complete_task(self, title: str) -> None:
        if title in self.tasks:
            self.tasks[title].complete()

    def remove_task(self, title: str) -> None:
        if title in self.tasks:
            del self.tasks[title]

    def display_tasks(self) -> None:
        for title, task in self.tasks.items():
            print(f"{title}: {task}")

    def get_tasks(self) -> List[Task]:
        return list(self.tasks.values())
