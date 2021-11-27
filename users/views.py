from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewCustomerForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewCustomerForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
