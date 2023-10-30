import uuid
from uuid import UUID
from datetime import datetime


class Task:
    """
    Représente une tâche avec un identifiant unique, un titre, une description, un statut de complétion et une date de création.
    
    Attributes:
        id (UUID): Identifiant unique de la tâche.
        title (str): Titre de la tâche.
        description (str): Description détaillée de la tâche.
        is_completed (bool): Indique si la tâche est complétée ou non.
        created_at (datetime): Date et heure de la création de la tâche.
    """
    def __init__(self, title: str, description: str) -> None:
        """
        Initialise un nouvel objet Task avec un titre, une description, un identifiant unique et une date de création.
        
        Args:
            title (str): Le titre de la tâche.
            description (str): La description de la tâche.
        """
        self.id: UUID = uuid.uuid4()  # Generate a unique id
        self.title: str = title
        self.description: str = description
        self.is_completed: bool = False
        self.created_at: datetime = datetime.now()

    def complete(self) -> None:
        """
        Indique la tâche comme complétée.
        """
        self.is_completed = True

    def __repr__(self) -> str:
        """
        Représente l'objet Task sous forme de chaîne de caractères.

        Returns:
            str: Représentation textuelle de l'objet Task.
        """
        return f"Task(id={self.id}, title={self.title}, description={self.description}, is_completed={self.is_completed}, created_at={self.created_at})"
