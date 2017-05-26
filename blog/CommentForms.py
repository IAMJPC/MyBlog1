from django import forms


class CommentForm(forms.Form):
    commentContext = forms.CharField(label='评论内容', error_messages={'required': '请填写您的评论'})