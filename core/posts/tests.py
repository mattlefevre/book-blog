from django.test import TestCase, SimpleTestCase
from users.models import CustomUser

# Create your tests here.
class LoggedOutResponseTests(TestCase):
    # Naming convention: test_{url_name}_page

    def test_accounts_page_status_code(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_status_code_logged_out(self):
        response = self.client.get("/new_post")
        self.assertEqual(response.status_code, 301)

    def test_update_post_page_status_code_logged_out(self):
        response = self.client.get("/update_post")
        self.assertEqual(response.status_code, 301)

    # NOTE: Need to add tests for the admin page, and then perform admin hardening.

class LoggedInResponseTests(TestCase):
    def set_up(self):
        self.credentials = {
            'email_address':'testuser@books-and-bones.com',
            'password':'a-secret-pw1!',
            'username':'testuername'
        }
        CustomUser.objects.create_user(**self.credentials)
    
    def test_login(self):
        self.set_up()
        #login
        response = self.client.post('accounts/login/', 
            **email=self.credentials['email_address'],
            **password=self.credentials['password'],follow=True)
        # should be logged in now
        self.assertTrue(response.context['CustomUser'].is_authenticated)
    
    def test_new_post_page_status_code_logged_in(self):
        self.set_up()
        response = self.client.post('accounts/login/', **self.credentials, follow=True)
        response = self.client.get("/new_post")
        self.assertEqual(response.status_code, 200)

    def test_update_post_page_status_code_logged_in(self):
        self.set_up()
        response = self.client.post('accounts/login/', **self.credentials, follow=True)
        response = self.client.get("/update_post")
        self.assertEqual(response.status_code, 200)