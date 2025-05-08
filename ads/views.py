# views.py
#from regis.views import Account 
from django.shortcuts import render, redirect
from .forms import DeveloperProfileForm

def collect(request):
    if request.method == 'POST':
        form = DeveloperProfileForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'collect.html', {'form': form, 'success': True})  # Show success message
    else:
        form = DeveloperProfileForm()

    return render(request, 'collect.html', {'form': form, 'success': False})