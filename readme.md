# 🧪 Proyecto de testing automatizado - SauceDemo

## 📌 Propósito del proyecto
El propósito de este proyecto es automatizar pruebas funcionales sobre la página https://www.saucedemo.com/, una plataforma demo utilizada para prácticas de testing automatizado.  

Las pruebas implementadas validan tres flujos principales del sitio:
- Login: Verifica la autenticación de usuarios válidos e inválidos.  
- Navegación del catálogo: Comprueba la visualización y acceso correcto a los productos.  
- Carrito de compras: Valida la adición del produto y el chequeo que del producto elegido  



## 🛠️ Tecnologías utilizadas

- Python
- Pytest → framework de testing automatizado  
- Selenium WebDriver → automatización del navegador  
- WebDriver Manager*→ gestión automática de drivers de Chrome/Firefox  
- Logging
- Faker
- CSV / JSON
- Request

## ⚙️ Instalación de dependencias

pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html
pip install faker

## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las prubas: **reporte HTML**, **capturas de pantalla**, **archivo de log**




## Como ejecutar las pruebas
python3 -m run_test.py


comandos utiles 
python3 -m pytest test/test_login.py -v
pytest -s test_login.py   --> muestra los print()
pytest -s  test/test_navegacion_catalogo.py 
 pytest -v  (desde el directorio raiz, debidoa  queno no toma alguno en particular) 

# ignora test
@pytest.mark.skip(reason="Clase ignorada")

# APIS
se agrega una api key particular para los test de la api reqres. Para poder testear de deberá cambiar desde el archivo conftest.py


## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejeucion mediante `run_test.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.

La arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas practicas y permitiendo su escalabilidad en el tiempo.










