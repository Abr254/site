from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

# Inline form definition
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']# Update this field list as needed


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
@login_required
def chat(request):
    user = request.user

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = user
            message.save()
            return redirect('chat')  # Redirect to prevent resubmission on refresh
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-timestamp')  # Show latest first

    return render(request, 'chat.html', {'form': form, 'messages': messages})
