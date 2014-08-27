from datetime import date

from django.db import models
from django.db.models import Sum
from django.utils.encoding import smart_str


# Create your models here.


class Player(models.Model):
    TEAM_CHOICES = (
        ("D1", "Damer 1"),
        ("D2", "Damer 2"),
        ("H1", "Herrer 1"),
        ("H2", "Herrer 2"),
    )

    POSITION_CHOICES = (
        ("K", "Keeper"),
        ("B", "Back"),
        ("S", "Senter"),
        ("L", "Løper"),
    )
    fornavn = models.CharField(max_length=50, null=False, blank=False)
    etternavn = models.CharField(max_length=50, null=False, blank=False)
    draktnummer = models.PositiveIntegerField(null=True, blank=True)
    posisjon = models.CharField(max_length=10, choices=POSITION_CHOICES, null=True, blank=True)
    lag = models.CharField(max_length=10, choices=TEAM_CHOICES)
    profilbilde = models.ImageField(upload_to="/static/media/uploads/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Spillere"

    def __str__(self):
        return smart_str(self.lag) + ' ' + smart_str(self.fornavn) + ' ' + smart_str(self.etternavn)


class Match(models.Model):
    hjemmelag = models.CharField(max_length=100)
    bortelag = models.CharField(max_length=100)
    sted = models.CharField(max_length=100)
    dato = models.DateTimeField()

    @property
    def is_past_due(self):
        if date.today() > self.date:
            return True
        return False

    class Meta:
        verbose_name_plural = "Kamper"

    def __str__(self):
        return smart_str(self.hjemmelag) + ' - ' + smart_str(self.bortelag)


class PlayerPoint(models.Model):
    spiller = models.ForeignKey(Player)
    kamp = models.ForeignKey(Match)
    mål = models.IntegerField()
    assist = models.IntegerField()
    utvisningsminutter = models.IntegerField()

    class Meta:
        verbose_name_plural = "Poeng"

    def __str__(self):
        return smart_str(self.spiller) + ' ' + smart_str(self.mål) + ' ' + smart_str(self.assist) + ' ' + smart_str(
            self.utvisningsminutter)


class Result(models.Model):
    kamp = models.ForeignKey(Match)
    mål_hjemmelag = models.IntegerField()
    mål_bortelag = models.IntegerField()

    class Meta:
        verbose_name_plural = "Resultater"

    def __str__(self):
        return smart_str(self.kamp) + '  ' + smart_str(self.mål_hjemmelag) + ' - ' + smart_str(self.mål_bortelag)





