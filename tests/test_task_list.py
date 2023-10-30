import pytest
from models import TaskList

def setup_function():
    """
    Fonction de configuration exécutée avant chaque test.
    
    Cette fonction initialise une nouvelle instance de la classe TaskList, 
    qui est stockée dans une variable globale pour être utilisée dans les fonctions de test.
    """
    global task_list
    task_list = TaskList()

def test_add_task():
    """
    Teste la capacité d'ajouter une nouvelle tâche à la liste des tâches.

    Ce test ajoute une tâche avec un titre et une description spécifiques.
    Il vérifie ensuite si la tâche a été correctement ajoutée à la liste 
    en s'assurant que le titre existe dans les tâches et que la description correspond.
    """
    task_list.add_task("Task1", "Description1")
    assert "Task1" in task_list.tasks
    assert "Description1" == task_list.tasks["Task1"].description

def test_complete_task():
    """
    Teste la capacité de marquer une tâche existante comme complétée.

    Ce test ajoute d'abord une tâche à la liste des tâches, puis la marque comme complétée.
    Il vérifie ensuite si le statut de la tâche a été correctement mis à jour comme étant complété.
    """
    task_list.add_task("Task1", "Description1")
    task_list.complete_task("Task1")
    assert task_list.tasks["Task1"].is_completed

def test_remove_task():
    """
    Teste la capacité de supprimer une tâche de la liste des tâches.

    Ce test ajoute d'abord une tâche à la liste des tâches, puis la supprime.
    Il vérifie ensuite si la tâche a été correctement supprimée de la liste.
    """
    task_list.add_task("Task1", "Description1")
    task_list.remove_task("Task1")
    assert "Task1" not in task_list.tasks

def test_display_tasks(capsys):
    """
    Teste la capacité d'afficher toutes les tâches de la liste.
    
    Ce test ajoute quelques tâches, puis appelle la méthode d'affichage.
    En utilisant le paramètre "capsys", il capture la sortie standard pour vérifier 
    si les tâches sont correctement affichées.
    """
    task_list.add_task("Task1", "Description1")
    task_list.add_task("Task2", "Description2")
    # Appel à la méthode d'affichage ici
    # Capture de la sortie standard
    # Asserts pour vérifier l'affichage correct des tâches
