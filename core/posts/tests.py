from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    # Naming convention: test_{url_name}_page

    def test_accounts_page_status_code(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_status_code(self):
        response = self.client.get("/new_post")
        self.assertEqual(response.status_code, 200)

    def test_update_post_page_status_code(self):
        response = self.client.get("/update_post")
        self.assertEqual(response.status_code, 200)

    # NOTE: Need to add tests for the admin page, and then perform admin hardening.
