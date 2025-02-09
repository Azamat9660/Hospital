from .models import Doctor
from django_filters import FilterSet



class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'service_price': ['gt', 'lt'],
            'specialty': ['exact'],

        }