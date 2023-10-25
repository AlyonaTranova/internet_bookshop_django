from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['user_id', 'post_id', 'text', 'rating']

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['user_id'].widget = forms.HiddenInput()
		self.fields['post_id'].widget = forms.HiddenInput()
