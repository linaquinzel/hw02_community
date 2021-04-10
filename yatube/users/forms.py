from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Введите имя")
    sender = forms.EmailField(label="Email для ответа")
    subject = forms.CharField(label="Тема сообщения", initial='Письмо администратору', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(label="Отправить себе копию", required=False)
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body') 


User = get_user_model()


class CreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")