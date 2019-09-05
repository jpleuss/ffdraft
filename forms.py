from django.forms import ModelForm, ModelChoiceField
from django_select2.forms import Select2Widget
from ffdraft.models import Draft, Player


class DraftForm(ModelForm):
    player = ModelChoiceField(
        queryset=Player.objects.exclude(draft__player__isnull=False),
        label=u"Draft",
        required=False, widget=Select2Widget)

    class Meta:
        model = Draft
        fields = ['player']
