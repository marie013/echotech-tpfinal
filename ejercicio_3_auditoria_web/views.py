from ejercicio_3_auditoria_web.metricas import obtener_metricas_consumo
from django.shortcuts import render

def vista_panel_sustentabilidad(request):
    registro_consumos= [
        {"planta": "Planta Norte", "consumo": 100 },
        {"planta": "Planta Sur", "consumo": 50 },
        {"planta": "Planta Norte", "consumo": 10 }
    ]

    consumos = obtener_metricas_consumo(registro_consumos)

    context = {
        "total_emisiones_global" : consumos["total_emisiones_global"],
        "planta_critica" : consumos["planta_mayor_consumo"],
        "lista_consumos": registro_consumos

    }
    return render(request, 'sustentabilidad/panel.html', context)

