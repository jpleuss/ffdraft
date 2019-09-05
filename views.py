from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django_tables2 import RequestConfig
from django.shortcuts import render
from ffdraft.models import Draft, Player
from ffdraft.tables import TeamList
from ffdraft.forms import DraftForm
import csv, io


def admindraftboard(request):
    drafttable = Draft.objects.all()
    context = {'drafttable': drafttable}
    return render(request, 'ffdraft/admindraftboard.html', context)

# full view for teams drafting, admin has edit function from "draftboard.html"
def fulldraftboard(request):
    drafttable = Draft.objects.all()
    context = {'drafttable': drafttable}
    return render(request, 'ffdraft/fullboard.html', context)


#View of the draftboard with the currently drafting team at the top
def draftboard(request):
    draft_list = list(Draft.objects.exclude(player__isnull=False))
    drafting = draft_list[0]
    x = drafting.id
    y = x-5

    drafttable = Draft.objects.exclude(player__isnull=False)
    drafted = Draft.objects.filter(pk__gte=y).filter(pk__lt=x)
    context = {
        'drafttable': drafttable,
        'drafted': drafted,
   }
    return render(request, 'ffdraft/draftboard.html', context)


#Form view to select player from Draft
class DraftUpdateView(LoginRequiredMixin, UpdateView):
    model = Draft
    form_class = DraftForm
    success_url = reverse_lazy('draftboard')

#Team view so that people can view who they already drafted onto their teams
def team_view(request, team):
    table = TeamList(Player.objects.filter(draft__draft_team=team))
    RequestConfig(request).configure(table)
    return render(request, 'ffdraft/team_view.html', {'table': table})


#Player board to show all players
def player_list(request):
    table = Player.objects.exclude(draft__player__isnull=False)
    return render(request, "ffdraft/player_list.html", {'table': table})

#Playerboard sorted by position
def position(request, POS):
    table = Player.objects.exclude(draft__player__isnull=False).filter(pos=POS)
    return render(request, "ffdraft/player_list.html", {'table': table})


#CSV upload form to bulk add Players
@permission_required('admin.can_add_log_entry')
def player_upload(request):
    template = "ffdraft/upload.html"

    prompt = {
        'order': "Order of csv should be rk, name, pos, bye"
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Draft.objects.update_or_create(
            rk=column[0],
            name=column[1],
            pos=column[2],
            bye=column[3]
        )

    context = {}
    return render(request, template, context)

