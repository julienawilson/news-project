from rest_framework import serializers
from articles.models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'short_desc',
            'long_desc',
            'link',
            'date_submitted',
            'votes',
            # 'tags'
        )