from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse
from users.models import CustomUser

# Naming convention: test_{url_name, not actual url}_page


class LoggedOutPostResponseTests(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("account_login"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_book_page_status_code(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_status_code_logged_out(self):
        response = self.client.get("/new_post/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("new_post"))
        self.assertEqual(response.status_code, 302)

    def test_update_post_page_status_code_logged_out(self):
        response = self.client.get("/update_post")
        self.assertEqual(response.status_code, 301)
        response = self.client.get(reverse("update_post"))
        self.assertEqual(response.status_code, 302)

    # NOTE: Need to add tests for the admin page, and then perform admin hardening.


class LoggedInResponseTests(TestCase):
    # NOTE: Gotta figure out how to test while logged in
    pass
