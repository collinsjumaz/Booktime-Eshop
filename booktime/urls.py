from django.contrib import admin
from django.urls import path, include
from main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact-us', views.ContactUsView.as_view(), name="contact_us"),
]
