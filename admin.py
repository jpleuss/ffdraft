from django.contrib import admin


from .models import Player, Draft


class DraftAdmin(admin.ModelAdmin):
    list_display = ('draft_round', 'draft_team')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rk')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Draft, DraftAdmin)
