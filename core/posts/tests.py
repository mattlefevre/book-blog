from django.test import Client, TestCase, SimpleTestCase
from users.models import CustomUser

# Naming convention: test_{url_name, not actual url}_page

class LoggedOutResponseTests(TestCase):

    def test_accounts_page_status_code(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_book_page_status_code(self):
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_status_code_logged_out(self):
        response = self.client.get("/new_post")
        self.assertEqual(response.status_code, 301)

    def test_update_post_page_status_code_logged_out(self):
        response = self.client.get("/update_post")
        self.assertEqual(response.status_code, 301)

    # NOTE: Need to add tests for the admin page, and then perform admin hardening.


class LoggedInResponseTests(TestCase):
    pass