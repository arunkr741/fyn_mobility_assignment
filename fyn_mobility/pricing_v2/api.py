from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from decimal import Decimal

class CalculatePricingAPI(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        data = request.data

        day = data.get("day", "monday")
        total_distance = Decimal(data.get("total_distance", 0))
        waiting_time = Decimal(data.get("waiting_time", 0))
        time_taken = Decimal(data.get('time_taken', 0))
        q = Q(**{"%s" % day: True })
        pricingConfig = PricingConfig.objects.filter(q ,is_enabled=True).order_by("-id").first()

        if pricingConfig:
            base_price = pricingConfig.distance_base_price
            additional_distance = total_distance - pricingConfig.base_distance
            time_multiplier = pricingConfig.time_multiplication_factor.filter(time__gte = time_taken).order_by('time').first()

            print(time_multiplier, "time")

            chargeable_waiting_time = waiting_time - pricingConfig.free_waiting_minutes
            waiting_charge=0
            if chargeable_waiting_time > 0:
                waiting_charge = chargeable_waiting_time * pricingConfig.waiting_charges
            
            total_price =( base_price) +(additional_distance * pricingConfig.distance_additional_price) +\
            (time_multiplier.time_multiplier_factor * time_taken ) + waiting_charge

            return Response({'price': total_price}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No pricing configuration available.'}, status=status.HTTP_400_BAD_REQUEST)



