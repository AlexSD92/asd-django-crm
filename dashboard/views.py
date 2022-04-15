from django.shortcuts import render
from flask import render_template

def render_dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def render_privacy_policy(request):
    return render(request, 'dashboard/privacy_policy.html')

def render_t_and_c(request):
    return render(request, 'dashboard/terms_and_conditions.html')
