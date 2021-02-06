
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Task

def createItem(client):
    url = reverse('task-create')
    data = {'title' : 'Walk the dog', 'completed': True}
    return client.post(url, data, format='json')


class TestCreateTodoItem(APITestCase):
    """
        Enusre we can create a new todo item
    """
    def setUp(self):
        self.response = createItem(self.client)

    def test_received_201_created_status_code(self):   
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_item_was_created(self):
        self.assertEqual(Task.objects.count(), 1)

    def test_item_has_correct_title(self):
        self.assertEqual(Task.objects.get().title, 'Walk the dog')
