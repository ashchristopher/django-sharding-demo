from django.contrib import admin

from records.models import Bill, Invoice


class BillAdmin(admin.ModelAdmin):
    pass

class InvoiceAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Bill, BillAdmin)
# admin.site.register(Invoice, InvoiceAdmin)
