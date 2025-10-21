from django.contrib import admin

from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'account_number', 'country', 'status', 'created_at')
    list_filter = ('status', 'country')
    search_fields = ('first_name', 'last_name', 'account_number')
