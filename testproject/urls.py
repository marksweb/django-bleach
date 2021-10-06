from django.urls import path

from .views import home, model_form


urlpatterns = [
    path('', home, name='home'),
    path('model_form/', model_form, name='model_form'),
]
