from django.shortcuts import render
from .models import PropertyDetails

def properties(request):
    if request.method =='GET':
        data = request.GET
        pr = data('price_range');
        pt = data('property_type');
        nh = data('neighorhood');

        properties = PropertyDetails.objects.filter(propert__pr=pr,propert__property_type=pt,propert__neighbhorhood=nh)

        data = {
            'properties': properties
        }

        return render(request, "properties.html", data)
        