from limpieza import limpiar_registro_sensor
from resumen_estadistico import generar_resumen_sensores

lista_sensores = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "sensor_002", "temperatura": " 30.2 °C ", "ubicacion": ""},
    {"sensor_id": " SENSOR-003", "temperatura": "19.8", "ubicacion": "Planta Sur "},
    {"sensor_id": "SENSOR-004 ", "temperatura": "22.0C", "ubicacion": "Depósito"},
    {"sensor_id": "sensor-005", "temperatura": "26.4C", "ubicacion": " Planta Norte"},
    {"sensor_id": " SENSOR-006 ", "temperatura": "35.4 c", "ubicacion": ""},
    {"sensor_id": "sensor_007", "temperatura": " 28.1 ", "ubicacion": "Laboratorio "},
    {"sensor_id": " SENSOR-008", "temperatura": "21.6C", "ubicacion": "Planta Sur"},
    {"sensor_id": "SENSOR-009 ", "temperatura": "18.9 °C", "ubicacion": ""},
    {"sensor_id": "sensor-010", "temperatura": " 25.0C ", "ubicacion": " Planta Baja "},
    {"sensor_id": " SENSOR-011 ", "temperatura": "29.3", "ubicacion": "Oficinas"},
    {"sensor_id": "sensor_012", "temperatura": "26.9°c", "ubicacion": ""},
    {"sensor_id": " SENSOR-013", "temperatura": "23.7C", "ubicacion": " Depósito "},
    {"sensor_id": "SENSOR-014 ", "temperatura": " 27.8 c ", "ubicacion": "Planta Norte"},
    {"sensor_id": "sensor-015", "temperatura": "N/D", "ubicacion": ""},
    {"sensor_id": " SENSOR-016 ", "temperatura": "31.0 °C", "ubicacion": " Laboratorio"},
    {"sensor_id": "sensor_017", "temperatura": " 22.4C ", "ubicacion": "Planta Sur"},
    {"sensor_id": " SENSOR-018", "temperatura": "19.2c", "ubicacion": ""},
    {"sensor_id": "SENSOR-019 ", "temperatura": "26.5C", "ubicacion": " Planta Baja"},
    {"sensor_id": "sensor-020", "temperatura": " 24.0 ", "ubicacion": "Oficinas "},
    {"sensor_id": " SENSOR-021 ", "temperatura": "29.8C", "ubicacion": ""},
    {"sensor_id": "sensor_022", "temperatura": "18.5 c", "ubicacion": "Depósito"},
    {"sensor_id": " SENSOR-023", "temperatura": " 33.1 °C ", "ubicacion": " Planta Norte "},
    {"sensor_id": "SENSOR-024 ", "temperatura": "21.2", "ubicacion": ""},
    {"sensor_id": "sensor-025", "temperatura": "25.6C", "ubicacion": "Laboratorio"},
    {"sensor_id": " SENSOR-026 ", "temperatura": " 27.0 ", "ubicacion": " Planta Sur"},
    {"sensor_id": "sensor_027", "temperatura": "25.8", "ubicacion": ""},
    {"sensor_id": " SENSOR-028", "temperatura": "22.8C", "ubicacion": "Oficinas "},
    {"sensor_id": "SENSOR-029 ", "temperatura": " 30.5 c", "ubicacion": "Depósito"},
    {"sensor_id": "sensor-030", "temperatura": "19.0", "ubicacion": ""},
    {"sensor_id": " SENSOR-031 ", "temperatura": "24.9 °C ", "ubicacion": " Planta Baja"},
    {"sensor_id": "sensor_032", "temperatura": " 28.4C", "ubicacion": "Planta Norte "},
    {"sensor_id": " SENSOR-033", "temperatura": "22.3c", "ubicacion": ""},
    {"sensor_id": "SENSOR-034 ", "temperatura": "23.1C", "ubicacion": "Laboratorio"},
    {"sensor_id": "sensor-035", "temperatura": " 32.0 ", "ubicacion": " Planta Sur "}
]

lista_sensores_limpios = []

#Limpieza de registro en los sensores
for registro in lista_sensores:
    sensor_limpio = limpiar_registro_sensor(registro)
    lista_sensores_limpios.append(sensor_limpio)

#Generar resumen estadístico
umbral_temperatura = 24.0

lista_sensores_alertas, promedio_temperatura = generar_resumen_sensores(
    lista_sensores_limpios,
    umbral_temperatura
)

#Muestra 1 Registros Normalizados
print("<< REGISTROS NORMALIZADOS >>")
for sensor in lista_sensores_limpios:
    print(sensor)
print("\n=================================================")
#Muestra 2 Resumen estadístico
print("<< REPORTE ECOTECH SOLUTIONS >>")
print(f"Total de sensores: {len(lista_sensores_limpios)}")
print(f"Temperatura Promedio: {promedio_temperatura}°C")

print("Sensores en alerta:")

if lista_sensores_alertas:
    for sensor_id in lista_sensores_alertas:
        print(f"- {sensor_id}")
else:
    print("No se detectaron alertas.")