from django import forms
from .models import Answer, Question, Profile

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class SearchForm(forms.Form):
	search_str = forms.CharField(max_length=100)

class RegisterForm(forms.Form):
	confirm = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Profile
		fields = ['username', 'nickname', 'email', 'password']

	def clear_password(self):
		data = super().clean()
		password = data.get('password')
		confirm = data.get('confirm')

		if password != confirm:
			raise forms.ValidationError("Password confirmation failed")
