from django.urls import path
from . import views

urlpatterns = [
    path('', views.pano_view, name='pano'),
]
