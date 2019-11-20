from django import forms
from .models import Review, Movie

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'score',)