from django.urls import path, include

from . import views

app_name = 'recaptcha'


urlpatterns = [
    path('', views.example, name='example'),
]
