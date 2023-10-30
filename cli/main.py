import os
import argparse
import requests
import json

BASE_URL = os.environ.get('TASK_API_BASE_URL', 'http://127.0.0.1:5000')


def create_task(args):
    """
    Envoie une requête POST pour créer une nouvelle tâche en utilisant les arguments fournis.
    
    Args:
        args (argparse.Namespace): Contient les attributs 'title' et 'description' de la tâche à créer.

    Variables:
        data (dict): Dictionnaire contenant le titre et la description de la tâche.
        r (Response): Réponse obtenue après la requête POST.
    """
    data = {'title': args.title, 'description': args.description}
    r = requests.post(f'{BASE_URL}/tasks', json=data)
    print(r.json())


def list_tasks(args):
    """
    Envoie une requête GET pour lister toutes les tâches.

    Args:
        args (argparse.Namespace): Arguments analysés (non utilisés dans cette fonction, mais présents pour la conformité).

    Variables:
        r (Response): Réponse obtenue après la requête GET.
        tasks (list): Liste des tâches obtenues de la réponse.
    """
    r = requests.get(f'{BASE_URL}/tasks')
    tasks = r.json()
    for task in tasks:
        print(task)


def complete_task(args):
    """
    Envoie une requête PUT pour marquer une tâche comme complétée.

    Args:
        args (argparse.Namespace): Contient l'attribut 'title' de la tâche à marquer comme complétée.

    Variables:
        r (Response): Réponse obtenue après la requête PUT.
    """
    r = requests.put(f'{BASE_URL}/tasks/{args.title}/complete')
    print(r.json())


def delete_task(args):
    """
    Envoie une requête DELETE pour supprimer une tâche.

    Args:
        args (argparse.Namespace): Contient l'attribut 'title' de la tâche à supprimer.

    Variables:
        r (Response): Réponse obtenue après la requête DELETE.
    """
    r = requests.delete(f'{BASE_URL}/tasks/{args.title}')
    print(r.json())


if __name__ == '__main__':
    """
    Point d'entrée principal du script. Configure le parseur d'arguments et gère les sous-commandes.
    
    Variables:
        parser (ArgumentParser): Parseur principal pour les arguments.
        subparsers (Action): Objet pour ajouter des sous-parseurs pour chaque action.
        args (Namespace): Arguments analysés par le parseur.
    """
    parser = argparse.ArgumentParser(
        description='CLI to interact with Task API')
    subparsers = parser.add_subparsers()

    parser_create = subparsers.add_parser('create', help='Create a new task')
    parser_create.add_argument('title', type=str, help='Title of the task')
    parser_create.add_argument(
        'description', type=str, help='Description of the task')
    parser_create.set_defaults(func=create_task)

    parser_list = subparsers.add_parser('list', help='List all tasks')
    parser_list.set_defaults(func=list_tasks)

    parser_complete = subparsers.add_parser(
        'complete', help='Mark a task as complete')
    parser_complete.add_argument(
        'title', type=str, help='Title of the task to complete')
    parser_complete.set_defaults(func=complete_task)

    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument(
        'title', type=str, help='Title of the task to delete')
    parser_delete.set_defaults(func=delete_task)

    args = parser.parse_args()
    args.func(args)
