from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

# Register the Message model in the admin interface
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'timestamp')  # Fields to display in the list view
    list_filter = ('timestamp', 'user')  # Filter by timestamp and user
    search_fields = ('text',)  # Allow searching by message text
    ordering = ('-timestamp',)  # Order by timestamp in descending order

admin.site.register(Message, MessageAdmin)