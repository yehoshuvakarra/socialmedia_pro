from django import forms
from .models import Article
# class ArticleCreateForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields =('title','body')

class ArticleCreateForm(forms.Form):
    title = forms.CharField(
    label = 'Enter Title',
    widget = forms.TextInput(
    attrs = {
    'placeholder': 'title',
    'class':'form-control'
            }
        )
    )

    body = forms.CharField(
    label = 'Enter Body',
    widget = forms.Textarea(
    attrs = {
    'placeholder' : 'body',
    'class': 'form-control',
    'rows':50,
    'columns':20
    }
    )
    )
