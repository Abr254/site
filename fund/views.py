from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
import random
import json
from regis.models import Account

from regis.models import Account  # Your custom user account model



@login_required
def spin(request):
    user_account = Account.objects.get(user=request.user)
    return render(request, 'spin.html', {'balance': user_account.balance})