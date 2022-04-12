from django.shortcuts import render
from flask import render_template

def render_dashboard(request):
    return render(request, 'dashboard/dashboard.html')
