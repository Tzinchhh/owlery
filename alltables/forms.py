from django import forms
from .models import TestForm, SignUp, Letters
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SendForm(forms.Form):
    send_to = forms.TextInput(attrs={
        "class" :"choose",
        "placeholder": "Tap to choose...",
        "name": "send_to"}
                              )

    blocnot = forms.CharField(widget=forms.Textarea)
    send_it =forms


class Test(forms.ModelForm):
    class Meta:
        model = TestForm
        fields = ['title', 'message']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    def clean_message(self):
        message = self.cleaned_data.get('message')
        return message


class SignUpForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        usr = self.cleaned_data.get('username')
        return usr

    def clean_upassword(self):
        usr = self.cleaned_data.get('password')
        return usr

    class Meta:
        model = SignUp
        fields = ['username', 'password']

class SendLetter(forms.ModelForm):

    class Meta:
        model = Letters
        fields = ['send_to', 'message']

    send_to = forms.CharField(widget=forms.TextInput(attrs={
        "class" :"choose",
        "placeholder": "Tap to choose...",
        "name": "send to"}
                              ))
    message = forms.CharField(widget=forms.TextInput(attrs={
        "class" :"choose",
        "placeholder": "Tap to choose...",
        "name": "message"}
                              ))
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'password']

