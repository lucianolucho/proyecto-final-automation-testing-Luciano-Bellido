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

## ⚙️ Instalación de dependencias

pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html

pip install faker


## Como ejecutar las pruebas

pytest -v run_test.py

python3 -m pytest test/test_login.py -v

pytest -s test_login.py   --> muestra los print()

 pytest -s  test/test_navegacion_catalogo.py 

 pytest -v  (desde el directorio raiz, debidoa  queno no toma alguno en particular) 

# ignora test
@pytest.mark.skip(reason="Clase ignorada")

# APIS
se agrega una api key particular para los test de la api reqres

test_carrito.py y test_navegacion_catalogo.py tienen el logindriver basico (configurar con otro mas avanzado)


para acceder a las apis de reqrest 


 headers = {"x-api-key": "reqres-free-v1"}
 headers = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}


ejecutar los test con marcador
pytest -m api -v
python3 -m  pytest -m api -v


