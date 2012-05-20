from django import forms
from django.conf import settings

from profiles.models import ShardInfo

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


class ShardInfoModelForm(forms.ModelForm):

    class Meta:
        model = ShardInfo

    def __init__(self, *args, **kwargs):
        super(ShardInfoModelForm, self).__init__(*args, **kwargs)
        self.fields['shard'] = forms.ChoiceField(choices=_shard_options)



