from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact-us', views.ContactUsView.as_view(), name="contact_us"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
