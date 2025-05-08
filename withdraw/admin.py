from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WithdrawalRequest

class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'phone_number')

    actions = ['approve_withdrawals', 'reject_withdrawals']

    def approve_withdrawals(self, request, queryset):
        for withdrawal in queryset:
            # Simulate M-Pesa withdrawal processing here
            success = mpesa_withdrawal(withdrawal.amount, withdrawal.phone_number)
            if success:
                withdrawal.status = 'Approved'
                withdrawal.save()
        self.message_user(request, "Selected withdrawal requests have been approved.")

    def reject_withdrawals(self, request, queryset):
        for withdrawal in queryset:
            withdrawal.status = 'Rejected'
            withdrawal.save()
        self.message_user(request, "Selected withdrawal requests have been rejected.")

admin.site.register(WithdrawalRequest, WithdrawalRequestAdmin)