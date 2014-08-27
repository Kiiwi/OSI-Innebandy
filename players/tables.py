import django_tables2 as tables
from .models import Player
from .models import Match


class PlayerTable(tables.Table):

    class Meta:
        model = Player

class MatchTable(tables.Table):

    class Meta:
        model = Match