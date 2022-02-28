from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(
        widget = forms.Textarea(attrs = {
            'placeholder': 'Enter your comment'
        })
    )

    
class ReplyForm(forms.Form):
    body = forms.CharField(
        widget = forms.Textarea(attrs = {
            'placeholder': 'Enter your reply'
        })
    )