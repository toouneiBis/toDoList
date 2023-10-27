from flask import request, jsonify, Flask, flash, render_template,redirect,url_for
from models import TaskList
from flask_login import login_user, login_required, logout_user, current_user
from api.models import db, User, Task

task_list = TaskList()

def init_app(app: Flask):
    @app.route('/', methods=['GET', 'POST'])
    def login():
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
        logout_user()
        flash("Logout successfully.", "success")
        return redirect(url_for("login"))
    
    @app.route('/add-task')
    @login_required
    def add_task_view():
        return render_template('task_form.html')
    
    @app.route('/all-tasks')
    @login_required
    def all_tasks_view():
        return render_template('tasks.html')
    
    # Api endpoints
    @app.route('/tasks', methods=['POST'])
    def add_task():
        data = request.get_json()
        task_list.add_task(data['title'], data['description'])
        new_task = Task(title=data['title'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'status': 'Task added'})

    @app.route('/tasks', methods=['GET'])
    def list_tasks():
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
        print(title)
        task_list.complete_task(title)
        task = Task.query.filter_by(title=title).first()
        if task:
            task.is_completed = True
            db.session.commit()
        return jsonify({'status': 'Task marked as completed'})

    @app.route('/tasks/<string:title>', methods=['DELETE'])
    def delete_task(title):
        task_list.remove_task(title)
        task = Task.query.filter_by(title=title).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        return jsonify({'status': 'Task deleted'})