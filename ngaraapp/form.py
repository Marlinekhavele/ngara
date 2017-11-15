from django import forms
from ngaraapp.models import Contact

class ContactForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName  = forms.CharField()
    email     = forms.EmailField()
    password  = forms.CharField(widget=forms.PasswordInput)  
    estate    = forms.CharField()
    Location  = forms.CharField()

    class Meta:
          model = Contact
          fields = ('firstName', 'lastName', 'email', 'password',  'estate', 'Location',)
