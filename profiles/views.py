import random
from decimal import Decimal

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from profiles.models import Business
from profiles.mixins import JSONResponseMixin
from records.models import Record


def _get_shards():
    shards = []
    for db_name, meta_info in settings.DATABASES.iteritems():
        if meta_info.get('LOGICAL_SHARD', False):
            shards.append(db_name)
    return sorted(shards)
_shards = _get_shards()


class MainView(TemplateView):
    template_name = 'profiles/main.html'

    def get(self, request):
        
        context = {
            'business_ids' : [int(i.pk) for i in Business.objects.all()],
            'shards' : _shards,
        }

        return self.render_to_response(context)


class AjaxMainView(JSONResponseMixin, MainView):
    
    def post(self, request):
        context = {}
        business_id = request.POST.get('business', None)
        
        if business_id:
            business = get_object_or_404(Business, pk=business_id)
            shard = business.shard

            qty = random.randrange(0,10)
            price = Decimal(str(random.uniform(0,10))[0:4])
            rec_type = random.choice(['invoice', 'bill'])

            Record.objects.using(shard).create(business=business, quantity=qty, amount=price, record_type=rec_type)

            for shard in _shards:
                context.update({
                    shard : Record.objects.using(shard).all().count(),
                })

        return self.render_to_response(context) 


class ShardInfoView(TemplateView):
    template_name = 'profiles/shard_info.html'

    def get(self, request, shard_id):
        records = Record.objects.using(shard_id).all()
        page = request.GET.get('page', 1)

        paginator = Paginator(records, 100)

        try:
            recs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            recs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            recs = paginator.page(paginator.num_pages)

        context = {
            'shard' : shard_id,
            'shard_records' : recs,
        }

        return self.render_to_response(context)

class BusinessView(TemplateView):
    template_name = 'profiles/business.html'

    def get(self, request, business_id):
        business = get_object_or_404(Business, pk=business_id)
        shard = business.shard

        context = {
            'business' : business,
            'bills' : business.bill_set.using(shard).all(),
            'invoices' : business.invoice_set.using(shard).all(),
            'accounts' : business.account_set.all(),
        }
        return self.render_to_response(context)

