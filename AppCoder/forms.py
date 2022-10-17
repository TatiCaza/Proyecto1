from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class form_cursos(forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()

class form_profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class form_entregable(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregada = forms.BooleanField()

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Last Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password']
        help_text = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':"Old Password"}))
    new_password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':"New Password"}))
    new_password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':"Confirm new password"}))
    

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_text = {k:"" for k in fields}