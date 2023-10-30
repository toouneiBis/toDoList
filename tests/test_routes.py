import json
from flask_testing import TestCase
from flask import Flask
import api.routes as routes
from models import TaskList

class TestTasksRoutes(TestCase):

    def create_app(self):
        app = Flask(__name__)
        routes.init_app(app)
        return app

    def setUp(self):
        self.client = self.create_app().test_client()
        self.task_list = TaskList()

    def test_add_task(self):
        response = self.client.post(
            '/tasks',
            data=json.dumps({'title': 'Task 2', 'description': 'Description 2'}),
            content_type='application/json'
        )
        self.assert200(response)
        self.assertEqual(response.get_json(), {'status': 'Task added'})

    def test_list_tasks(self):
        response = self.client.get('/tasks')
        self.assert200(response)
        # Expecting a single task because of setUp
        self.assertEqual(len(response.get_json()), 1)

    def test_complete_task(self):
        response = self.client.put('/tasks/Task 1/complete')
        self.assert200(response)
        self.assertEqual(response.get_json(), {'status': 'Task marked as completed'})

    def test_delete_task(self):
        response = self.client.delete('/tasks/Task 1')
        self.assert200(response)
        self.assertEqual(response.get_json(), {'status': 'Task deleted'})
