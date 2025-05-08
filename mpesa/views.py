from django.shortcuts import render, redirect
from django.http import JsonResponse
from mpesa.forms import MpesaTransactionForm
from .models import MpesaTransaction

def mpesa(request):
    form = MpesaTransactionForm()

    if request.method == 'POST':
        form = MpesaTransactionForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            
            access_token = get_mpesa_access_token()
            if access_token is None:
                return JsonResponse({'status': 'error', 'message': 'Failed to authenticate with MPESA API.'})

            response = initiate_mpesa_deposit(phone_number, amount, access_token)

            MpesaTransaction.objects.create(
                phone_number=phone_number,
                amount=amount,
                status='Success' if response.get('status') == 'success' else 'Failed'
            )

            if response.get('status') == 'success':
                return JsonResponse({'status': 'success', 'amount': amount})
            else:
                return JsonResponse({'status': 'error', 'message': 'Deposit failed, please try again.'})

    return render(request, 'mpesa.html', {'form': form})