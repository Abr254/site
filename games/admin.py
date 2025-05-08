from django.contrib import admin
from .models import Earnings

@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = ['user', 'site', 'quiz', 'score', 'earned', 'created_at']
    list_filter = ['created_at', 'site']
    search_fields = ['user__username', 'site', 'quiz']