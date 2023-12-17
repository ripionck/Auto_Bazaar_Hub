from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','text']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'text': 'Comments',  
        }
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['rows'] = 5 