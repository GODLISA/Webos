from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Field, Layout, Row, Submit
from .models import Usuario, Receta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Row(
                    Column('username', css_class="col-md-12"),
                    Column('email', css_class="col-md-12"),
                    Column('password1', css_class="col-md-12"),
                    Column('password2', css_class="col-md-12")
                )
            )
        )

class RecipeFormClass(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'titulo',
            'imagen',
            'parrafo',
            'usuario'
        ]
        labels = {
            'titulo' : 'Titulo',
            'imagen' : 'Imagen',
            'parrafo' : 'Describe tu deliciosa receta',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class' : 'form-control'
                },
            ),
            'parrafo': forms.Textarea(
                attrs={
                    'class' : 'form-control'
                },
            ),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Row(
                    Column('titulo', css_class='col-md-12'),
                    Column('parrafo', css_class='col-md-12'),
                    Column('imagen', css_class='col-md-12'),
                    Submit(
                        'submit', 'Hornear',
                        css_class='btn btn-primary btn-lg float-right'
                    ),
                    css_class='col-md-6'
                ),
                css_class='d-flex justify-content-center'
            ),
            Field('usuario', type='hidden')
        )

class LoginFormClass(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Row(
                    Column('username', css_class='col-md-12'),
                    Column('password', css_class='col-md-12'),
                    Submit(
                        'submit', 'Login',
                        css_class='btn btn-primary btn-lg float-right'
                    ),
                    css_class='col-md-6'
                ),
                css_class='d-flex justify-content-center',
            )
        )

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electronico',
            'password': 'Contraseña'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class' : 'form-control'
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class' : 'form-control'
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class' : 'form-control'
                },
            ),
            'email': forms.EmailInput(
                attrs={
                    'class' : 'form-control'
                },
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class' : 'form-control'
                },
            )
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Row(
                    Column('username', css_class='col-md-12'),
                    Column('first_name', css_class='col-md-12'),
                    Column('last_name', css_class='col-md-12'),
                    Column('email', css_class='col-md-12'),
                    Column('password', css_class='col-md-12'),
                    Submit(
                        'submit', 'Registrar',
                        css_class='btn btn-primary btn-lg float-right'
                    ),
                    css_class='col-md-6'
                ),
                css_class='d-flex justify-content-center'
            )
        )
    
    def save(self, commit=True):
        user = super(UserRegister, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user