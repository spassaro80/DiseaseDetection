from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login') + '?registered'
    def get_form(self, form_class=None):
        form = super(SignUpView,self).get_form()
        #modificar formulario en tiempo de ejecución
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Username'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Repeat Password'})
        form.fields['username'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        form.fields['username'].help_text = ''
        form.fields['password1'].help_text = ''
        form.fields['password2'].help_text = ''

        return form