
from django.conf.urls import url
from articles.views import PostArticleView, ArticleDetail

urlpatterns = [
    url(r'^post/$', PostArticleView.as_view(), name='post_article'),
    url(r'^(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article_detail')
]
