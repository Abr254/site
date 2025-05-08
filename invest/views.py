from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from regis.models import Account
from decimal import Decimal

@login_required
def invest(request):
    user_account = Account.objects.get(user=request.user)

    if request.method == 'POST':
        try:
            amount = float(request.POST.get('amount'))
        except (ValueError, TypeError):
            messages.error(request, "Please enter a valid amount.")
            return redirect('invest')

        if amount < 100:
            messages.error(request, "Minimum investment is Ksh100.")
            return redirect('invest')

        if amount > float(user_account.balance):
            messages.error(request, "Insufficient balance for this investment.")
            return redirect('invest')

        # Determine the refund percentage
        if 100 <= amount <= 200:
            refund_percent = 105
        elif 300 <= amount <= 400:
            refund_percent = 110
        elif 500 <= amount <= 600:
            refund_percent = 115
        elif 700 <= amount <= 800:
            refund_percent = 120
        elif 900 <= amount <= 1000:
            refund_percent = 130
        elif amount >= 1100:
            refund_percent = 150
        else:
            messages.error(request, "Invalid amount range for investment terms.")
            return redirect('invest')

        expected_return = round(amount * refund_percent / 100, 2)

        # Deduct balance safely using Decimal
        user_account.balance -= Decimal(str(amount))
        user_account.save()

        messages.success(
            request,
            f"Investment of Ksh{amount} submitted successfully. "
            f"You will receive Ksh{expected_return} in 10 days."
        )
        return redirect('invest')

    return render(request, 'invest.html', {'account': user_account})