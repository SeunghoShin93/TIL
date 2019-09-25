from django import forms
from .models import Article, Comment
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10, 
#     label='제목', 
#     widget=forms.TextInput(attrs={
#         'class': 'my-title', 
#         'placeholder': 'Enter the title',
#         }
#         )
#     ) 
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(attrs={
#             'class': 'my-content',
#             'placeholder': 'Enter the content',
#             'rows': 5,
#             'cols': 50,
#     }))

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=10, 
    label='제목', 
    widget=forms.TextInput(attrs={
        'class': 'my-title', 
        'placeholder': 'Enter the title',
        }
        )
    ) 
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'my-content',
            'placeholder': 'Enter the content',
            'rows': 5,
            'cols': 50,
    }))
    class Meta:
        model = Article
        # fields = ('title', 'content',)
        fields = '__all__'
        #exclude = ('title')
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'

            
        #     })
        # }

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=140)
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
    class Meta:
        model = Comment
        fields ='__all__'