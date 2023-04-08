from django import forms
from .models import News

class AddArticle(forms.ModelForm):
    title = forms.CharField(label='title', max_length=100)
    text = forms.Textarea()

    class Meta:
        model = News
        fields = ('title', 'text',)