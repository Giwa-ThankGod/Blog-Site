from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(
        widget = forms.Textarea(attrs = {
            'class': 'form',
            'placeholder': 'send your comment'
        })
    )

    
class ReplyForm(forms.Form):
    body = forms.CharField(
        widget = forms.Textarea(attrs = {
            'class': 'form',
            'placeholder': 'send your reply'
        })
    )