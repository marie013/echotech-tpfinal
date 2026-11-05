# echotech-tpfinal
# EcoTech Solutions

Proyecto del Trabajo Final Integrador de Python orientado al desarrollo de soluciones tecnológicas para la gestión y el análisis de datos relacionados con la sustentabilidad.

El proyecto está dividido en tres ejercicios independientes, cada uno enfocado en diferentes conceptos de programación y desarrollo de software.

# Objetivos

- Procesar y normalizar datos provenientes de sensores.
- Gestionar un catálogo de productos mediante programación orientada a objetos.
- Analizar métricas de sustentabilidad y emisiones.
- Aplicar buenas prácticas de programación, modularización y testing.

## 🛠️ Tecnologías utilizadas

- Python
- Django
- Pytest
- HTML y CSS (para la interfaz web)

# Estructura del proyecto

ecotech-tpfinal/
│
├── config/
│
├── ejercicio_1_sensores/
│   ├── limpieza.py
│   ├── resumen_estadistico.py
│   └── main.py
│
├── ejercicio_2_productos/
│   ├── excepciones.py
│   ├── dispositivos.py
│   ├── gestor_inventario.py
│   ├── catalogo_ecotech.json
│   └──main.py
│
├── ejercicio_3_auditoria_web/
│   ├── calculos.py
│   ├── metricas.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── sustentabilidad/
│   │       └── panel.html
│   ├── static/
│   │   └── ejercicio_3_auditoria_web/
│   │       └── css/
│   │           └── panel.css
│   └── tests/
│       ├── test_emisiones.py
│       └── test_metricas.py
│
├── .gitignore
├── catalogo_ecotech.json
├── manage.py
├── requirements.txt
├── pytest.ini
└── README.md


# Ejercicios

# 1. Procesamiento de datos de sensores

Módulo encargado de procesar registros de sensores y generar información estadística.

Funcionalidades:
- Limpieza y normalización de registros.
- Conversión de temperaturas a valores numéricos.
- Asignación de ubicaciones predeterminadas.
- Identificación de sensores que superan un umbral de temperatura.
- Cálculo de temperatura promedio.


# 2. Gestión de productos

Módulo orientado a la gestión de un catálogo de productos mediante programación orientada a objetos.


# 3. Auditoría web y métricas de sustentabilidad

Módulo destinado al análisis de métricas web y su relación con indicadores de sustentabilidad.



# Instalación y configuración

Clonar el repositorio:

git clone marie013/echotech-tpfinal


Ingresar al directorio:


cd ecotech-tpfinal


Crear y activar un entorno virtual:

python -m venv venv


En Windows:

venv\Scripts\activate


Instalar las dependencias:

pip install -r requirements.txt


# Ejecución

Para ejecutar el primer ejercicio desde la raíz del proyecto:

python -m ejercicio_1_sensores.main


#  Pruebas

Ejecutar todos los tests con:

pytest ejercicio_3_auditoria_web/tests/ -v

