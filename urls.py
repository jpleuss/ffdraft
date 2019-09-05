from django.urls import path
from ffdraft.views import (
    draftboard,
    DraftUpdateView,
    admindraftboard,
    player_upload,
    player_list,
    position,
    fulldraftboard,
    team_view,
)


urlpatterns = [
    path('', draftboard, name='draftboard'),
    path('draft/<int:pk>/', DraftUpdateView.as_view(), name='update_draft'),
    path('fullboard/', fulldraftboard, name='fullboard'),
    path('players/', player_list, name='player_list'),
    path('position/<POS>', position, name='position'),
    path('teams/<team>', team_view, name='team_view'),
    path('admindraftboard', admindraftboard, name='admindraftboard'),
    path('upload-csv/', player_upload, name='player_upload'),
]

