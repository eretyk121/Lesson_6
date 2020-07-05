from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
    def clean_text(self):
        cleaned_data = self.cleaned_data['text']
        return cleaned_data

