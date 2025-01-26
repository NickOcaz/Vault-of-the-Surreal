from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Comment, Rating

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='sonic', password='nick1971')

    def test_user_registration(self):
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        response = self.client.post(reverse('account_login'), {
            'login': 'sonic',
            'password': 'nick1971',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_logout(self):
        logged_in = self.client.login(username='sonic', password='nick1971')
        self.assertTrue(logged_in)
        response = self.client.post(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)
        # Make another request to check authentication status
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class MovieDatabaseTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='sonic', password='nick1971')
        self.movie = Movie.objects.create(
            title='Test Movie',
            slug='test-movie',
            year=1980,
            director='Test Director',
            description='Test Description',
            status=1
        )

    def test_movie_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')

    def test_movie_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.movie.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')

class UserReviewsAndRatingsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='sonic', password='nick1971')
        self.movie = Movie.objects.create(
            title='Test Movie',
            slug='test-movie',
            year=1980,
            director='Test Director',
            description='Test Description',
            status=1
        )
        self.client.login(username='sonic', password='nick1971')

    def test_add_comment(self):
        response = self.client.post(reverse('post_detail', args=[self.movie.slug]), {
            'body': 'Great movie!',
            'comment_form': 'Submit Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(body='Great movie!').exists())

    def test_add_rating(self):
        response = self.client.post(reverse('post_detail', args=[self.movie.slug]), {
            'score': 8,
            'rating_form': 'Submit Rating'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Rating.objects.filter(score=8).exists())

class CommunityInteractionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='sonic', password='nick1971')
        self.movie = Movie.objects.create(
            title='Test Movie',
            slug='test-movie',
            year=1980,
            director='Test Director',
            description='Test Description',
            status=1
        )
        self.comment = Comment.objects.create(
            movie=self.movie,
            author=self.user,
            body='Great movie!',
            approved=True
        )

    def test_approve_comment(self):
        self.client.login(username='sonic', password='nick1971')
        response = self.client.post(reverse('approve_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)

    def test_delete_comment(self):
        self.client.login(username='sonic', password='nick1971')
        response = self.client.post(reverse('comment_delete', args=[self.movie.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())