from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_dashboard, name='main-dashboard'),
    path('privacy_policy.html/', views.render_privacy_policy, name='privacy_policy'),
    path('terms_and_conditions.html/', views.render_t_and_c, name='terms_and_conditions'),
]
