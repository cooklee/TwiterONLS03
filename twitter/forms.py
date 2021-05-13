from django import forms

from twitter.models import Tweet, Message


class TweetCreationForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }


class MessageCreationForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['to_user', 'text']
