from ejercicio_3_auditoria_web.calculos import calcular_emisiones_carbono

def obtener_metricas_consumo(registros):
    if not registros:
        return {"total_emisiones_global": 0, "planta_mayor_consumo": "Ninguna"}

    total_emisiones_global = 0
    consumo_por_planta= {}
    planta_mayor_consumo= ""

    for i in registros:
        consumo = i["consumo"]
        planta = i["planta"]

        total_emisiones_global += calcular_emisiones_carbono(consumo)

        if planta not in consumo_por_planta:
            consumo_por_planta[planta] = 0

        consumo_por_planta[planta] += consumo

    planta_mayor_consumo = max(
        consumo_por_planta,
        key=consumo_por_planta.get
    )

    return {
            "total_emisiones_global": total_emisiones_global,
            "planta_mayor_consumo": planta_mayor_consumo
        }