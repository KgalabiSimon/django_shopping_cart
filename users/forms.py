from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Customer


class NewCustomerForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", 'email')

    def save(self, commit=True):
        user = super(NewCustomerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
