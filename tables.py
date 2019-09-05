import django_tables2 as tables
from ffdraft.models import Player

class TeamList(tables.Table):
    rnd = tables.Column(accessor='draft.draft_round')
    class Meta:
        model = Player
        sequence = ('pos', 'name', 'rk', 'bye', 'rnd')
        template_name = 'django_tables2/bootstrap.html'

