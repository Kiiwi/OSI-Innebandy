from django.contrib import admin

# Register your models here.

from .models import Player
from .models import Match
from .models import PlayerPoint
from .models import Result


class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        model = Player

admin.site.register(Player, PlayerAdmin)


class MatchAdmin(admin.ModelAdmin):
    class Meta:
        model = Match

admin.site.register(Match, MatchAdmin)


class PlayerPointAdmin(admin.ModelAdmin):
    class Meta:
        model = PlayerPoint

admin.site.register(PlayerPoint, PlayerPointAdmin)


class ResultAdmin(admin.ModelAdmin):
    class Meta:
        model = Result

admin.site.register(Result, ResultAdmin)