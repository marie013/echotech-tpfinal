from ejercicio_3_auditoria_web.metricas import obtener_metricas_consumo


def test_obtener_metricas_consumo():
    registros = [
        {"planta": "Planta Norte", "consumo": 100},
        {"planta": "Planta Sur", "consumo": 50},
        {"planta": "Planta Norte", "consumo": 10}
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["total_emisiones_global"] == 64.0
    assert resultado["planta_mayor_consumo"] == "Planta Norte"


def test_obtener_metricas_sin_registros():
    resultado = obtener_metricas_consumo([])

    assert resultado["total_emisiones_global"] == 0
    assert resultado["planta_mayor_consumo"] == "Ninguna"