from ejercicio_2_productos.dispositivos import DispositivoEcologico, PanelSolar
from ejercicio_2_productos.excepciones import StockInvalidoError
from ejercicio_2_productos.gestor_inventario import GestorInventario


#Creando instancias de dos objetos
dispositivo = DispositivoEcologico(
    id_producto=1,
    nombre="Panel Solar",
    precio=150000,
    stock=10
)
panel = PanelSolar(
    id_producto=1,
    nombre="Panel Solar MAX",
    precio=240000,
    stock=5,
    eficiencia=60,
    potencia_w=600
)



dispositivo.stock = 15
print("Stock actualizado:", dispositivo.stock)


inventario_prueba=[dispositivo, panel]

#Prueba 1
try:
    disp_1= DispositivoEcologico(3, "Bateria Solar", 50000, 40)
    inventario_prueba.append(disp_1)
except StockInvalidoError as e:
    print(f"Error al crear el objeto: {e}")
#Prueba 2 para atrapar la excepción personalizada
try:
    disp_2= DispositivoEcologico(4, "Torre Hidropónico", 1500000, -15)
    inventario_prueba.append(disp_2)
except StockInvalidoError as e:
    print(f"Error al crear el objeto: {e}")


print("CATÁLOGO DE PRODUCTOS")
print(dispositivo.generar_ficha_tecnica())
print(panel.generar_ficha_tecnica())
#Persistencia con json

archivo = "catalogo_ecotech.json"
GestorInventario.guardar_catalogo_json(inventario_prueba, archivo)

print("Catálogo guardado correctamente")