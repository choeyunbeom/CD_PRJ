from django import forms
from crime.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "image",
        )

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = [
            "post",
            "content",
        ]

        widgets = {
            "content":forms.Textarea(
                attrs = {
                    "placeholder": "댓글달기...",
                }
            )
        }