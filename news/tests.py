from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu454', text = 'bnasjhdolah soldfha pshd')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_title = f'{post.title}'
        excepted_text = f'{post.text}'
        self.assertEqual(excepted_title, 'Mavzu454')
        self.assertEqual(excepted_text, 'bnasjhdolah soldfha pshd')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text = 'boshqa yangilik')

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_views_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')