from django import forms
from gui.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'imagen', 'resumen','content',)