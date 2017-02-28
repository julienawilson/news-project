from django import forms
from articles.models import Article


class ArticleForm(forms.ModelForm):
    """Form to make new Articles."""

    class Meta:
        model = Article
        fields = ['title', 'link']