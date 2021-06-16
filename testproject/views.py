from __future__ import absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import OperationalError

from .models import Person
from .forms import BleachForm, PersonForm


def home(request):
    if request.POST:
        form = BleachForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = BleachForm()

    return render(request, 'home.html', {'form': form})


def model_form(request):

    if request.POST:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?ok')
    else:
        form = PersonForm()
        try:
            people = list(Person.objects.all())
        except OperationalError:
            people = []

        return render(request, 'model_form.html', {
            'form': form,
            'people': people,
        })
