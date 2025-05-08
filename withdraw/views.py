from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from regis.models import Account
from .forms import WithdrawalForm
from withdraw.models import WithdrawalRequest

# Placeholder function for M-Pesa withdrawal (simulated)
def mpesa_withdrawal(amount, phone_number):
    # In a real application, you would integrate with an M-Pesa API here.
    print(f"Initiating M-Pesa withdrawal of Ksh{amount} to phone number: {phone_number}")
    return True  # Simulating a successful transaction.

@login_required
def feenax(request):
    user_account = Account.objects.get(user=request.user)
    return render(request, 'feenax.html', {'balance': user_account.balance})

@login_required
def withdraw(request):
    user_account = Account.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            withdrawal_amount = form.cleaned_data['amount']
            
            if withdrawal_amount <= user_account.balance:
                # Create a withdrawal request and save it
                withdrawal_request = WithdrawalRequest(
                    user=request.user,
                    amount=withdrawal_amount,
                    phone_number=user_account.phone_number  # Corrected
                )
                withdrawal_request.save()

                # Deduct balance
                user_account.balance -= withdrawal_amount
                user_account.save()
                
                # Notify user
                messages.success(request, f"Your withdrawal request for Ksh{withdrawal_amount} has been submitted and is pending approval.")
                return redirect('withdraw')
            else:
                messages.error(request, "Insufficient balance.")
        else:
            messages.error(request, "Invalid amount entered.")
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html', {'form': form, 'account': user_account})