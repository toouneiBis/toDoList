from flask import request, jsonify, Flask, flash, render_template,redirect,url_for
from models import TaskList
from flask_login import login_user, login_required, logout_user, current_user
from api.models import db, User, Task

task_list = TaskList()

def init_app(app: Flask):
    """
    Initialise les routes de l'application Flask.
    """
    @app.route('/', methods=['GET', 'POST'])
    def login():
        """
        Traite et affiche la page de connexion.

        Si un utilisateur est déjà authentifié, il est redirigé vers la page de toutes les tâches.
        Sinon, la méthode traite les demandes HTTP GET et POST :

        - GET : Affiche la page de connexion.
        - POST : Traite les informations du formulaire de connexion fournies. Si les informations sont correctes, 
                 l'utilisateur est authentifié et redirigé vers la page de toutes les tâches. Sinon, un message d'erreur 
                 est affiché.

        Attentes du corps du formulaire POST (lors de la soumission) :
        {
            'username': 'Nom d'utilisateur',
            'password': 'Mot de passe de l'utilisateur'
        }

        :return: Redirige vers la page de toutes les tâches si l'utilisateur est authentifié. Sinon, renvoie 
                 le rendu de la page de connexion avec les éventuels messages d'erreur.
        """
        if current_user.is_authenticated:
            return redirect(url_for("all_tasks_view"))
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            print(user)
            if user and user.check_password(password):
                login_user(user)
                flash('Login successful.', 'success')
                return redirect(url_for('all_tasks_view'))
            else:
                flash('Invalid username or password. Please try again.', 'danger')
        return render_template('login.html')
    
    @app.route("/logout")
    @login_required
    def logout():
        """
        Déconnecte l'utilisateur actuellement authentifié.

        Après la déconnexion, l'utilisateur est redirigé vers la page de connexion avec un message indiquant 
        que la déconnexion a été réussie.

        :return: Redirige vers la page de connexion après la déconnexion de l'utilisateur.
        """
        logout_user()
        flash("Logout successfully.", "success")
        return redirect(url_for("login"))
    
    @app.route('/add-task')
    @login_required
    def add_task_view():
        """
        Affiche le formulaire pour ajouter une nouvelle tâche.

        Cette vue est accessible uniquement aux utilisateurs authentifiés. Elle renvoie le rendu du modèle de 
        formulaire permettant à l'utilisateur de saisir les détails d'une nouvelle tâche.

        :return: Rendu du modèle de formulaire d'ajout de tâche.
        """
        return render_template('task_form.html')
    
    @app.route('/all-tasks')
    @login_required
    def all_tasks_view():
        """
        Affiche la liste de toutes les tâches.

        Cette vue est accessible uniquement aux utilisateurs authentifiés. Elle renvoie le rendu du modèle 
        présentant la liste de toutes les tâches que l'utilisateur a créées.

        :return: Rendu du modèle affichant toutes les tâches.
        """
        return render_template('tasks.html')
    
    # Api endpoints
    @app.route('/tasks', methods=['POST'])
    def add_task():
        """
        Ajoute une nouvelle tâche à la base de données.

        Accepte une requête POST contenant les détails de la tâche au format JSON. 
        Crée une nouvelle tâche dans la base de données avec les détails fournis.

        :param: title: Titre de la tâche.
        :param: description: Description de la tâche.
        :return: Un objet JSON indiquant le succès de l'ajout de la tâche.
        """
        data = request.get_json()
        task_list.add_task(data['title'], data['description'])
        new_task = Task(title=data['title'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'status': 'Task added'})

    @app.route('/tasks', methods=['GET'])
    def list_tasks():
        """
        Renvoie une liste de toutes les tâches stockées dans la base de données.

        Interroge la base de données pour toutes les tâches et renvoie les détails 
        de chaque tâche sous forme d'une liste d'objets JSON.

        :return: Un objet JSON contenant une liste de tâches.
        """
        tasks = task_list.get_tasks()
        tasks = Task.query.all()
        all_tasks = [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'is_completed': task.is_completed,
            'created_at': task.created_at.strftime("%Y-%m-%d %H:%M:%S")
            } for task in tasks]
        return jsonify(all_tasks)

    @app.route('/tasks/<string:title>/complete', methods=['PUT'])
    def complete_task(title):
        """
        Marque une tâche spécifique comme complétée.

        Accepte une requête PUT et met à jour le statut de la tâche dans la base de données 
        pour la marquer comme complétée.

        :param title: Titre de la tâche à marquer comme complétée.
        :return: Un objet JSON indiquant le succès de la mise à jour du statut de la tâche.
        """
        print(title)
        task_list.complete_task(title)
        task = Task.query.filter_by(title=title).first()
        if task:
            task.is_completed = True
            db.session.commit()
        return jsonify({'status': 'Task marked as completed'})

    @app.route('/tasks/<string:title>', methods=['DELETE'])
    def delete_task(title):
        """
        Supprime une tâche spécifique de la base de données.

        Accepte une requête DELETE et supprime la tâche correspondante de la base de données.

        :param title: Titre de la tâche à supprimer.
        :return: Un objet JSON indiquant le succès de la suppression de la tâche.
        """
        task_list.remove_task(title)
        task = Task.query.filter_by(title=title).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        return jsonify({'status': 'Task deleted'})