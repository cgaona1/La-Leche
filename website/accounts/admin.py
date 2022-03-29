from django.contrib import admin

from .models import Notification

# Register your models here.
class NotificationFormAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')

admin.site.register(Notification, NotificationFormAdmin)
