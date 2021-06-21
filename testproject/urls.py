try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from .views import (home, model_form)

urlpatterns = [
    url('^$', home, name='home'),
    url('^model_form$', model_form, name='model_form'),
]
