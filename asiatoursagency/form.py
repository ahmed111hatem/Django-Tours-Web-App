from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  message = forms.CharField( widget=forms.Textarea)
  
  def SendEmail(self):
    print(f"Sending From {self.cleaned_data['email']} With Message: {self.cleaned_data['message']}")

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            raise forms.ValidationError("The passwords do not match!")
        return cleaned_data
