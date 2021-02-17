from django import forms
from . import models
from .models import *

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'image')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'class':'editable medium-editor-textarea postcontent'}),

        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')
        labels = {
            'author': '',
            'text': ''
        }
        
        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass postcomment',
                                             'placeholder':'Author',
                                             'label':''
                                             }),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcomment',
                                           'placeholder':'Text',
                                           }),
        }
        


