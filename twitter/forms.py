from django import forms

from twitter.models import Tweet


class TweetCreationForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }
