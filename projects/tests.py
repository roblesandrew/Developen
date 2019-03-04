
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from .views import delete_account

class UserAccountTests(TestCase):
	def setUp(self):
		create_account_form_data = {
			'firstname': 'Oski', 
			'lastname': 'Bear', 
			'username': 'oskibear', 
			'password': 'top_secret'
		}

		self.factory = RequestFactory()
		self.client.post('/projects/create-account/', create_account_form_data)
		

	def test_create_user(self):
		user = User.objects.get(username='oskibear')

		self.assertEqual(user.username, 'oskibear')

	def test_delete_user(self):
		user = User.objects.get(username='oskibear')
		request = self.factory.get('/projects/delete-account/')
		request.user = user

		delete_account(request)
		user_list = User.objects.filter(username='oskibear')

		self.assertEqual(len(user_list), 0) 





