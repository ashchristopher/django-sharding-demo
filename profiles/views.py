from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from profiles.models import Business


class BusinessView(TemplateView):
    template_name = 'profiles/index.html'

    def get(self, request, business_id):
        business = get_object_or_404(Business, pk=business_id)
        shard = business.shardinfo.shard

        context = {
            'business' : business,
            'bills' : business.bill_set.using(shard).all(),
            'invoices' : business.invoice_set.using(shard).all(),
            'accounts' : business.accounts.all(),
        }
        return self.render_to_response(context)
