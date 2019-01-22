from django import forms
from .models import Answer, Question, Profile


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

class QuestionForm(forms.ModelForm):
    tags = forms.CharField(max_length=300, initial="", required=True)

    class Meta:
        model = Question
        fields = ['title', 'text']

class SearchForm(forms.Form):
    search_str = forms.CharField(max_length=100)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = [  'username', 'nickname', 'email', 'upload', 'password']
    
    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class SettingsForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'nickname', 'email', 'upload']
        # widgets = {
        #     'username': forms.TextInput(attrs={'readonly': 'readonly'})
        # }