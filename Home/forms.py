from django import forms
from .models import Suscriber, Contact

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
       
