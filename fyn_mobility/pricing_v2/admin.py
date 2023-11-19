from django.contrib import admin
from .models import PricingConfig, TimeMultiplicationFactor

admin.site.register(PricingConfig)
admin.site.register(TimeMultiplicationFactor)