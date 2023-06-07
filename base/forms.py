from django.forms import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.utils.translation import gettext_lazy as _
from .models import Profile
from .models import CustomUser
from django.core.exceptions import ValidationError


# Signupform
class SignUpX(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name': 'username',
            'class': 'credentialinput',
            'type': 'text',
            'placeholder': 'Username.',
            'required': 'required',
        })
        self.fields["first_name"].widget.attrs.update({
            'first_name': 'first_name',
            'class': 'credentialinputshort',
            'type': 'text',
            'placeholder': 'Firstname',
            'required': 'required',
        })
        self.fields["last_name"].widget.attrs.update({
            'last_name': 'last_name',
            'class': 'credentialinputshort',
            'type': 'text',
            'placeholder': 'Lastname',
            'required': 'required',
        })
        self.fields["email"].widget.attrs.update({
            'email': 'email',
            'class': 'credentialinput',
            'type': 'text',
            'placeholder': 'Email',
            'required': 'required',
            })
        self.fields["password1"].widget.attrs.update({
            'password1': 'password1',
            'class': 'credentialinput',
            'type': 'text',
            'placeholder': 'Password..',
            'required': 'required',
        })
        self.fields["password2"].widget.attrs.update({
            'password2': 'password2',
            'class': 'credentialinput',
            'type': 'text',
            'placeholder': 'Confirm..',
            'required': 'required',
        })

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']
              
# recovermail
class RecoverX(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'username': 'username',
            'class': 'credentialinput',
            'type': 'text',
            'placeholder': 'Recovery email',
            'required': 'required',
            })

# updateuser
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name': 'username',
            'class': 'login-input',
            'type': 'text',
            'placeholder': 'Username.',
            'required': 'required',
        })
        self.fields["email"].widget.attrs.update({
            'email': 'email',
            'class': 'login-input',
            'type': 'text',
            'placeholder': 'Email.',
            'required': 'required',
        })

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

# updateprofile
class UpdateProfileForm(forms.ModelForm):
    profilepic = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['profilepic']
        
#passordrestform
class CustomPasswordResetForm(PasswordResetForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'forminput2',
            'placeholder': 'Enter new password',
            'required': 'true'
        }),
        strip=False
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'forminput2',
            'placeholder': 'Confirm new password',
            'required': 'true'
        }),
        strip=False
    )

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return new_password2


#editexcelrecordform
class TransactionForm(forms.Form):
    date = forms.DateField(label='Date')