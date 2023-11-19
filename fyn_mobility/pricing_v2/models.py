from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class TimeMultiplicationFactor(models.Model):
    time_multiplier_factor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    time = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


class PricingConfig(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    distance_base_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    base_distance = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    free_waiting_minutes = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    distance_additional_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    time_multiplication_factor = models.ManyToManyField(TimeMultiplicationFactor)
    
    waiting_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    monday = models.BooleanField(null=True, blank=True, default=False)
    tuesday = models.BooleanField(null=True, blank=True, default=False)
    wednesday = models.BooleanField(null=True, blank=True, default=False)
    thursday = models.BooleanField(null=True, blank=True, default=False)
    friday = models.BooleanField(null=True, blank=True, default=False)
    saturday = models.BooleanField(null=True, blank=True, default=False)
    sunday = models.BooleanField(null=True, blank=True, default=False)

    is_enabled = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
