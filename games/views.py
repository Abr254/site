from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Earnings
from django.db.models import Sum
from datetime import timedelta, date
import json

@login_required
def chart(request):
    today = date.today()
    last_month = today - timedelta(days=30)

    # Bar Chart: Earnings over the last 30 days (by date)
    earnings_data = Earnings.objects.filter(user=request.user, created_at__date__gte=last_month)\
        .values('created_at__date')\
        .annotate(total_earnings=Sum('earned'))\
        .order_by('created_at__date')

    dates = [entry['created_at__date'].isoformat() for entry in earnings_data]
    earnings = [float(entry['total_earnings']) for entry in earnings_data]

    # Pie Chart: Earnings grouped by site
    site_data = Earnings.objects.filter(user=request.user)\
        .values('site')\
        .annotate(total_earned=Sum('earned'))\
        .order_by('-total_earned')

    sites = [entry['site'] or 'Unknown' for entry in site_data]
    site_earnings = [float(entry['total_earned']) for entry in site_data]

    # Total earnings
    total_earnings = sum(site_earnings)

    return render(request, 'chart.html', {
        'dates': json.dumps(dates),
        'earnings': json.dumps(earnings),
        'sites': json.dumps(sites),
        'site_earnings': json.dumps(site_earnings),
        'total_earnings': total_earnings,
    })