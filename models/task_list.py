from typing import Dict, List
from .task import Task


class TaskList:
    """
    Représente une liste de tâches, permettant l'ajout, la complétion, la suppression et l'affichage des tâches.
    
    Attributes:
        tasks (Dict[str, Task]): Dictionnaire contenant les tâches, où la clé est le titre de la tâche et la valeur est l'objet Task correspondant.
    """
    def __init__(self) -> None:
        """
        Initialise un nouvel objet TaskList avec un dictionnaire de tâches vide.
        """
        self.tasks: Dict[str, Task] = {}

    def add_task(self, title: str, description: str) -> None:
        """
        Ajoute une nouvelle tâche à la liste des tâches.
        
        Args:
            title (str): Le titre de la tâche.
            description (str): La description de la tâche.
        """
        task = Task(title, description)
        self.tasks[title] = task

    def complete_task(self, title: str) -> None:
        """
        Marque une tâche comme complétée si elle existe dans la liste.
        
        Args:
            title (str): Le titre de la tâche à compléter.
        """
        if title in self.tasks:
            self.tasks[title].complete()

    def remove_task(self, title: str) -> None:
        """
        Supprime une tâche de la liste si elle existe.
        
        Args:
            title (str): Le titre de la tâche à supprimer.
        """
        if title in self.tasks:
            del self.tasks[title]

    def display_tasks(self) -> None:
        """
        Affiche toutes les tâches dans la liste sous la forme "titre: objet de tâche".
        """
        for title, task in self.tasks.items():
            print(f"{title}: {task}")

    def get_tasks(self) -> List[Task]:
        """
        Renvoie une liste de tous les objets de tâche présents dans le dictionnaire de tâches.

        Returns:
            List[Task]: Une liste contenant tous les objets Task.
        """
        return list(self.tasks.values())
