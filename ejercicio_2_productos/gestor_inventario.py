import json
from .dispositivos import PanelSolar

class GestorInventario():
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializar= []
        
        for disp in lista_dispositivos:
            datos_disp={
            "id_producto": disp.id_producto,
            "nombre": disp.nombre,
            "precio": disp.precio,
            "stock": disp.stock
            }

            if isinstance(disp, PanelSolar):
                datos_disp["eficiencia"] = disp.eficiencia
                datos_disp["potencia_w"] = disp.potencia_w
            datos_serializar.append(datos_disp)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializar, archivo, indent=4, ensure_ascii=False)
