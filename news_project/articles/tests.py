from django.test import TestCase, Client, RequestFactory

from articles.models import Article
# Create your tests here.


class ArticleTestCase(TestCase):
    """The Article App Test Runner."""

    def setUp(self):
        """Setup for tests."""
        self.client = Client()
        self.request = RequestFactory()

    def test_new_article_has_title(self):
        """Test that a newly created article has a title."""
        article = Article(title="Jedha Destroyed By First Order", link="http://starwars.wikia.com/wiki/Jedha")
        self.assertTrue(article.title == "Jedha Destroyed By First Order")
