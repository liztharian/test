from django import forms
from home.models import Post,Comment

class HomeForm(forms.ModelForm):
    post= forms.CharField()


    class Meta:
        model= Post
        fields=('post','title')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
