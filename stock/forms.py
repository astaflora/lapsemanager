from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


