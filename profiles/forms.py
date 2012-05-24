from django import forms
from django.conf import settings

from profiles.models import Business

def shard_options():
    choices = [
        ('', '--------'),
    ]

    for db_name, meta_info in settings.DATABASES.iteritems():
        if meta_info.get('LOGICAL_SHARD', False):
            choices.append(
                (db_name, db_name, )
            )
    choices = sorted(choices, key=lambda x: x)
    return choices
_shard_options = shard_options()


class BusinessModelForm(forms.ModelForm):

    class Meta:
        model = Business

    def __init__(self, *args, **kwargs):
        super(BusinessModelForm, self).__init__(*args, **kwargs)
        self.fields['shard'] = forms.ChoiceField(choices=_shard_options)



