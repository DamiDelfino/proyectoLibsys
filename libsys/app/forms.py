from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model, authenticate



User = get_user_model()



class FormularioLogin(forms.Form):

    username = forms.CharField(required = True)
    password = forms.CharField(widget = forms.PasswordInput, required = True)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)

            if not user:
                raise forms.ValidationError('Usuario inexistente')
            
            if not user.check_password(password):
                raise forms.ValidationError('Contraseña incorrecta')
            
            if not user.is_active:
                raise forms.ValidationError('Usuario inactivo, contacte con el administrador')
        
        return super(FormularioLogin, self).clean(*args, **kwargs)




class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]