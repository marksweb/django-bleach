from django.db import OperationalError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BleachForm, PersonForm
from .models import Person


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
