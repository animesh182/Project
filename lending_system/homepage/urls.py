from django.urls import path
from os import name
from .views import HomePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index', HomePageView.as_view(), name="Home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+= staticfiles_urlpatterns()