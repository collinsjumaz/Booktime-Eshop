from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from main import models
from main import views


urlpatterns = [
    path('about-us/',TemplateView.as_view(template_name="about_us.html")),
    path( "",TemplateView.as_view(template_name="home.html")),
    path("product/<slug:slug>/", DetailView.as_view(model=models.Product), name="product",),
]
