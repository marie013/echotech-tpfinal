
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta=[]
    
    suma_temperatura=0.0

    if not lista_sensores_limpios:
        return [], 0.0 
    
    for i in lista_sensores_limpios:

        temperatura=i["temperatura"]

        suma_temperatura+=temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(
                i["sensor_id"]
        )
    promedio_temperatura = round(suma_temperatura/len(lista_sensores_limpios), 2)
        
    return lista_sensores_alerta, promedio_temperatura
