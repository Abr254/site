from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Referral

@login_required
def invite(request):
    user = request.user
    
    # Retrieve all referrals for the user
    referrals = Referral.objects.filter(referrer=user)
    
    # If there are no referrals, create a new one
    if not referrals.exists():
        referral = Referral.objects.create(referrer=user)
    else:
        # Use the first referral if there are existing referrals
        referral = referrals.first()

    # Generate the invite link
    invite_link = f"https://feenax.onrender.com/?referral_code={referral.invite_code}"

    # Get the number of referrals excluding the current referral
    referral_count = referrals.exclude(id=referral.id).count()

    # Determine the level based on the referral count
    if referral_count >= 10:
        level = 3
    elif referral_count >= 3:
        level = 2
    else:
        level = 1

    # Send invite link via email or display it for sharing
    return render(request, 'invite.html', {'invite_link': invite_link, 'referral_count': referral_count, 'level': level})