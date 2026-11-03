
def limpiar_registro_sensor(registro_raw):

    sensor_id = registro_raw.get("sensor_id", "").strip().upper()

    temp_raw = registro_raw.get("temperatura", 0.0)

    if isinstance(temp_raw, (int, float)):
        temperatura = float(temp_raw)

    else:
        temp_str = str(temp_raw).strip().upper()

        temp_str = (
            temp_str.replace("°C", "")
                    .replace("°F", "")
                    .replace("C", "")
                    .replace("F", "")
                    .replace("°", "")
                    .strip()
        )

        try:
            temperatura = float(temp_str)

        except ValueError:
            temperatura = 0.0

    
    ubicacion = registro_raw.get("ubicacion", "")

    if isinstance(ubicacion, str) and ubicacion.strip():
        ubicacion = ubicacion.strip()
    else:
        ubicacion = "Área No Asignada"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }




