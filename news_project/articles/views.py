from django.views.generic import CreateView, DetailView, TemplateView
from django.utils import timezone
from django.shortcuts import redirect

from articles.models import Article
from articles.forms import ArticleForm


class TagView(TemplateView):

    template_name = "articles/tag_list.html"

    def get_context_data(self, tag):
        """Extending get_context_data method to add our data."""
        articles = Article.objects.filter(tags__slug=tag).all()
        return {'articles': articles,
                'tag': tag}


class PostArticleView(CreateView):

    model = Article
    form_class = ArticleForm
    template_name = "articles/post_article.html"

    def form_valid(self, form):
        """Execute if form is valid."""
        article = form.save()
        article.date_submitted = timezone.now()
        article.save()
        return redirect('home')


class ArticleDetail(DetailView):

    model = Article
    template_name = "articles/article_detail.html"
