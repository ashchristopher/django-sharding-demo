from django.contrib import admin

from profiles.models import Business, ShardInfo


class BusinessAdmin(admin.ModelAdmin):
    pass

class ShardInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Business, BusinessAdmin)
admin.site.register(ShardInfo, ShardInfoAdmin)
