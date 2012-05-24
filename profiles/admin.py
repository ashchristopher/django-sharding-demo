from django.contrib import admin

from profiles.models import Business
from profiles.forms import BusinessModelForm


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'shard',)
    form = BusinessModelForm


admin.site.register(Business, BusinessAdmin)
