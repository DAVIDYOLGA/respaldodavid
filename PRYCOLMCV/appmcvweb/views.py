from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView

from django.http import HttpResponse, JsonResponse

from .models import inicio

# para tomar en cuenta en la ordenacion y filtro de datos
# internamientos = Internamiento.objects.order_by('Cuarto').filter(
#    Q(fecha_egreso__gt=datetime.now()) | Q(fecha_egreso__isnull=True)
# )

# Create your views here.

class Inicio(TemplateView):
    template_name = 'appmcvweb/inicio.html'

    def get_context_data(self, *args, **kwargs):
        inicios = inicio.objects.all()
        #presentaciones = presentacion.objects.all()
        #comunicados = comunicado.objects.all()
        return {'inicios': inicios,}

