from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="用户名", max_length=32, widget=forms.TextInput(
        attrs={'placeholder': '用户名'}))
    password = forms.CharField(
        label="密码", max_length=128, widget=forms.PasswordInput(
            attrs={'placeholder': '密码'}))