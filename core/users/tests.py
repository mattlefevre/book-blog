from django.test import TestCase

# Create your tests here.


class LoggedOutUserResponseTests(TestCase):
    def test_reviewers_page_status_code(self):
        response = self.client.get("/reviewers/")
        self.assertEqual(response.status_code, 200)
