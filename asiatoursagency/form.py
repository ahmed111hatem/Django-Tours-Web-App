from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  message = forms.CharField( widget=forms.Textarea)
  
  def SendEmail(self):
    print(f"Sending From {self.cleaned_data['email']} With Message: {self.cleaned_data['message']}")
    