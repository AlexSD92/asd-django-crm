from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_dashboard, name='main-dashboard'),
]
