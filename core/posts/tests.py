from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse
from users.models import CustomUser
from posts.models import Post,Book

# Naming convention: test_{url_name, not actual url}_page


class LoggedOutPostResponseTests(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get(reverse("account_login"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get(reverse("posts:home"))
        self.assertEqual(response.status_code, 200)

    def test_book_page_status_code(self):
        response = self.client.get(reverse("posts:books"))
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_status_code_logged_out(self):
        response = self.client.get(reverse("posts:new_post"))
        self.assertEqual(response.status_code, 302)

    def test_update_post_page_status_code_logged_out(self):
        response = self.client.get(reverse("posts:update_post",kwargs={"username":"test","slug":"test-123"}))
        self.assertEqual(response.status_code, 302)

    # NOTE: Need to add tests for the admin page, and then perform admin hardening.


class PostOnlyModelTest(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            username="testusername",
            password="test123",
            email="test@test.test"
        )

        Post.objects.create(
            post_title="Test Title",
            post_contents="test contents",
            poster=CustomUser.objects.get(id=1)
            )

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.post_title}"
        self.assertEqual(expected_object_name, "Test Title")
    
    def test_post_poster(self):
        post = Post.objects.get(id=1)
        expected_poster = f"{post.poster}"
        self.assertEqual(expected_poster, "testusername")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_content = f"{post.post_contents}"
        self.assertEqual(expected_content, "test contents")

class PostAndBookModelTest(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            username="testusername",
            password="test123",
            email="test@test.test"
        )

        Book.objects.create(
            author="Test Author",
            title="The Best Book Ever",
            synopsis="I included a synopsis",
            isbn="123456789",
            rating=1,
        )

        Post.objects.create(
            post_title="Test Title",
            post_contents="test contents",
            poster=CustomUser.objects.get(id=1),
            book=Book.objects.get(id=1)
            )

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.post_title}"
        self.assertEqual(expected_object_name, "Test Title")
    
    def test_post_poster(self):
        post = Post.objects.get(id=1)
        expected_poster = f"{post.poster}"
        self.assertEqual(expected_poster, "testusername")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_content = f"{post.post_contents}"
        self.assertEqual(expected_content, "test contents")

    def test_post_book_author(self):
        post = Post.objects.get(id=1)
        expected_author = f"{post.book.author}"
        self.assertEqual(expected_author, "Test Author")

    def test_post_book_title(self):
        post = Post.objects.get(id=1)
        expected_title = f"{post.book.title}"
        self.assertEqual(expected_title, "The Best Book Ever")
    
    def test_post_book_synopsis(self):
        post = Post.objects.get(id=1)
        expected_synopsis = f"{post.book.synopsis}"
        self.assertEqual(expected_synopsis, "I included a synopsis")
    
    def test_post_book_isbn(self):
        post = Post.objects.get(id=1)
        expected_isbn = f"{post.book.isbn}"
        self.assertEqual(expected_isbn, "123456789")
    
    def test_post_book_rating(self):
        post = Post.objects.get(id=1)
        expected_rating = f"{post.book.rating}"
        self.assertEqual(expected_rating, "1")

class LoggedInResponseTests(TestCase):
    # NOTE: Gotta figure out how to test while logged in
    pass
