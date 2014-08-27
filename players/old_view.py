from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
from django.views.generic import ListView

# Create your views here.

from .forms import PlayerForm
from .forms import MatchForm

from .models import Player
from .models import Match
from .models import Result
from .models import PlayerPoint


def player(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("pages/form.html",
                              locals(),
                              context_instance=RequestContext(request))


def match(request):
    form = MatchForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("pages/form.html",
                              locals(),
                              context_instance=RequestContext(request))


class D1(ListView):
    context_object_name = "players"
    template_name = "d1.html"
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(D1, self).get_context_data(**kwargs)
        context["matches"] = Match.objects.all()
        context["results"] = Result.objects.all()
        context["player_point"] = PlayerPoint.objects.all()
        return context


class D2(ListView):
    context_object_name = "players"
    template_name = "d2.html"
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(D2, self).get_context_data(**kwargs)
        context["matches"] = Match.objects.all()
        context["results"] = Result.objects.all()
        context["player_point"] = PlayerPoint.objects.all()
        return context


class H1(ListView):
    context_object_name = "players"
    template_name = "h1.html"
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(H1, self).get_context_data(**kwargs)
        context["matches"] = Match.objects.all()
        context["results"] = Result.objects.all()
        context["player_point"] = PlayerPoint.objects.all()
        return context


class H2(ListView):
    context_object_name = "players"
    template_name = "h2.html"
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(H2, self).get_context_data(**kwargs)
        context["matches"] = Match.objects.all()
        context["results"] = Result.objects.all()
        context["player_point"] = PlayerPoint.objects.all()
        return context