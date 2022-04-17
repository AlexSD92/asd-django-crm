from django.shortcuts import render
from flask import render_template
from .models import Account
from django.contrib.auth.decorators import login_required

accounts = [
    {
        'business_name': 'Commify',
        'account_owner': 'Alex Dominguez'
    }
]

@login_required
def render_dashboard(request):
    context = {
        'accounts': Account.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)

def render_privacy_policy(request):
    return render(request, 'dashboard/privacy_policy.html')

def render_t_and_c(request):
    return render(request, 'dashboard/terms_and_conditions.html')
