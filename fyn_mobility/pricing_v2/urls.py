from django.urls import path
from .api import CalculatePricingAPI
from .views import manage_pricing_config

urlpatterns = [
    path('manage-pricing-config/', manage_pricing_config, name='manage-pricing-config'),
    path('calculate-pricing/', CalculatePricingAPI.as_view(), name='calculate-pricing'),
]


