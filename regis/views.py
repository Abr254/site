from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from withdraw.forms import WithdrawalForm
from regis.models import Account
from django.conf import settings
from withdraw.models import WithdrawalRequest


# Dashboard view
@login_required
def feenax(request):
    try:
        user_account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        messages.error(request, "Account not found. Please contact support.")
        return redirect('register')
    return render(request, 'feenax.html', {'balance': user_account.balance})


# Notification page
@login_required
def notify(request):
    return render(request, 'notify.html')


# Login view
def user_login(request):
    if request.user.is_authenticated:
        return redirect('feenax')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('feenax')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field in form.errors:
                messages.error(request, f"{field.capitalize()} error: {form.errors[field]}")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Registration view
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(user=user)  # Critical step
            messages.success(request, 'Registration successful! A Ksh200 bonus has been credited to your account. You can now log in.')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, f"{field.capitalize()} error: {form.errors[field]}")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# Logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('home')


# Withdraw view
@login_required
def withdraw(request):
    try:
        user_account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        messages.error(request, "Account not found. Please contact support.")
        return redirect('feenax')

    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            withdrawal_amount = form.cleaned_data['amount']
            if withdrawal_amount <= user_account.balance:
                WithdrawalRequest.objects.create(
                    user=request.user,
                    amount=withdrawal_amount,
                    phone_number=request.user.phone_number
                )
                user_account.balance -= withdrawal_amount
                user_account.save()
                messages.success(request, f"Withdrawal request for Ksh{withdrawal_amount} submitted successfully.")
                return redirect('withdraw')
            else:
                messages.error(request, "Insufficient balance.")
        else:
            messages.error(request, "Invalid amount entered.")
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html', {'form': form, 'account': user_account})