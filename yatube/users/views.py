from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup") #  где signup — это параметр "name" в path()
    template_name = "signup.html"


def user_contact(request):
    contact = Contact.objects.get(pk=3)
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    