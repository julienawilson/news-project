from django.views.generic import ListView

from articles.models import Article


class HomeView(ListView):

    model = Article
    template_name = "news_project/home.html"
    context_object_name = "articles"
