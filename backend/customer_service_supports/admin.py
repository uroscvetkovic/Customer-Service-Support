from django.contrib import admin

from .models import CustomerServiceSupport

@admin.register(CustomerServiceSupport)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_time_callback', 'submited_at', 'archived' )
    sortable_by = ('date_time_callback', 'submited_at')
    list_filter = ['archived']
