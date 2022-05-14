from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'input',
        })
    )
    email = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'input',
        })
    )
    message = forms.CharField(
        widget = forms.Textarea(attrs = {
            'class': 'input',
        })
    )


class ReplyForm(forms.Form):
    rname = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'input',
            'id': 'reply_name',
        })
    )
    remail = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'input',
            'id': 'reply_email',
        })
    )
    rmessage = forms.CharField(
        widget = forms.Textarea(attrs = {
            'class': 'input',
            'id': 'reply_message',
        })
    )
