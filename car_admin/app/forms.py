from django import forms
from .models import Review, Car

from ckeditor.widgets import CKEditorWidget


# class CarAdminForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['car', 'id', ]
#     def clean(self):
#         cleaned_data = self.cleaned_data['id']
#         return cleaned_data


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']
