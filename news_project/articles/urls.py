
from django.conf.urls import url
from articles.views import PostArticleView, ArticleDetail, TagView, ArticleListAPIView, ArticleDetailAPIView

urlpatterns = [
    url(r'^post/$', PostArticleView.as_view(), name='post_article'),
    url(r'^(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^(?P<tag>\w+)/$', TagView.as_view(), name='tag_list'),
    url(r'^api/list/$', ArticleListAPIView.as_view(), name='post_article'),
    url(r'^api/(?P<pk>\d+)/$', ArticleDetailAPIView.as_view(), name='article_detail'),
]
