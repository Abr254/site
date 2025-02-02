from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Home page view (this will render the home template)


# Home page view after login (Redirect if user is logged in)
@login_required
def feenax(request):
    return render(request, 'feenax.html')

# Notification page view (requires login)
@login_required
def notify(request):
    return render(request, 'notify.html')

# Login view
def user_login(request):
    # If the user is already logged in, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('feenax')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('feenax')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')  # Specific error for failed login
        else:
            # Handle invalid form case
            for field in form.errors:
                error_message = form.errors[field]
                if field == 'username':
                    messages.error(request, f"Invalid username: {error_message}")
                elif field == 'password':
                    messages.error(request, f"Invalid password: {error_message}")
                else:
                    messages.error(request, f"Error in {field}: {error_message}")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Registration view
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form and create a new user
            form.save()
            messages.success(request, 'Registration successful! A $2 bonus will be credited to your account. You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            # Handle invalid form case with specific error messages
            for field in form.errors:
                error_message = form.errors[field]
                if field == 'username':
                    messages.error(request, f"Username error: {error_message}")
                elif field == 'password1' or field == 'password2':
                    messages.error(request, f"Password error: {error_message}")
                elif field == 'phone_number':
                    messages.error(request, f"Phone number error: {error_message}")
                else:
                    messages.error(request, f"Error in {field}: {error_message}")

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('home')  # Redirect to login page after logout
    