from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('index', TemplateView.as_view(template_name='magazine/index.html')),
    path('main1', TemplateView.as_view(template_name='magazine/trend2020.html')),
    path('main2', TemplateView.as_view(template_name='magazine/Elsa.html')),
    path('main3', TemplateView.as_view(template_name='magazine/trip_trend.html')),
    path('Feb', TemplateView.as_view(template_name='magazine/Feb.html')),
    path('airport', TemplateView.as_view(template_name='magazine/airport.html')),
]