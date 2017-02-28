
from django.conf.urls import url
from articles.views import PostArticleView

urlpatterns = [
    url(r'^post/$', PostArticleView.as_view(), name='post_article'),
]
