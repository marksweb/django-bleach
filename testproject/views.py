from __future__ import absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BleachForm


def home(request):
    if request.POST:
        form = BleachForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = BleachForm()

    return render(request, 'home.html', {'form': form})
