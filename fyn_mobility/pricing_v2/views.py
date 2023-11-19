from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from .serializers import PricingConfigSerializer
from .forms import PricingConfigForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework.views import APIView

def manage_pricing_config(request):
    pricing_configs = PricingConfig.objects.all()

    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            pricing_config = form.save(commit=False)
            pricing_config.created_by = request.user
            pricing_config.save()

            # Redirect to the pricing configurations page
            return redirect('pricing-configurations')
    else:
        form = PricingConfigForm()

    return render(request, 'manage_pricing_config.html', {'form': form, 'pricing_configs': pricing_configs})

