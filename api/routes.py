```
from flask import request, jsonify, Flask
from models import TaskList

task_list = TaskList()

def init_app(app: Flask):
    @app.route('/tasks', methods=['POST'])
    def add_task():
        data = request.get_json()
        task_list.add_task(data['title'], data['description'])
        return jsonify({'status': 'Task added'})

    @app.route('/tasks', methods=['GET'])
    def list_tasks():
        tasks = task_list.get_tasks()
        return jsonify([str(task) for task in tasks])

    @app.route('/tasks/<string:title>/complete', methods=['PUT'])
    def complete_task(title):
        task_list.complete_task(title)
        return jsonify({'status': 'Task marked as completed'})

    @app.route('/tasks/<string:title>', methods=['DELETE'])
    def delete_task(title):
        task_list.remove_task(title)
        return jsonify({'status': 'Task deleted'})
 
```
