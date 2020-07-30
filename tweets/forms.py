from django import forms
from .models import Tweet

Max_Tweet_Length = 256

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > Max_Tweet_Length:
            raise forms.ValidationError("This Tweet is Too Long")
        return content
