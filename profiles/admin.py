from django.contrib import admin

from profiles.models import Business, ShardInfo
from profiles.forms import ShardInfoModelForm


class ShardInfoInline(admin.StackedInline):
    model = ShardInfo
    form = ShardInfoModelForm


class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        ShardInfoInline,
    ]

admin.site.register(Business, BusinessAdmin)
# admin.site.register(ShardInfo, ShardInfoAdmin)
