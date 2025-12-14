from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils import datos 
from utils import lector_json 

import time
import pytest


RUTA_JSON = "datos/productos.json"

@pytest.mark.skip(reason="Clase ignorada")
#@pytest.mark.parametrize("usuario,password,debe_funcionar",datos.leer_csv_login("datos/login.csv"))
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",lector_json.leer_json_productos(RUTA_JSON))

def test_carrito_json(login_in_driver ,usuario,password,nombre_producto):
    try:
          driver = login_in_driver
          catalogo = InventoryPage(driver)

          #Obtengo los productos de la página
          productos = catalogo.obtener_productos()
          print(f'Se encontraron {len(productos)} productos.')
          #print(productos)

          #Añadir un producto al carrito haciendo clic en el botón correspondiente
          nombre_producto =  catalogo.seleccionarProductoByIndice(0)
          
          print(f' El nombre del producto seleccionado es {nombre_producto}')     

          #Verificar que el contador del carrito se incremente correctamente

          contador = int(catalogo.obtener_contador_carrito())      
                
          assert contador == 1 , "contador incorrecto"
          print("El contador se incrementó correctamnete")

          #Navegar al carrito de compras
          catalogo.ir_al_carrito()           


          #Comprobar que el producto añadido aparezca correctamente en el carrito
          carrito = CartPage(driver) 
          producto_comprado = carrito.obtenerProductoEnCarritoById(0)

          assert  producto_comprado == nombre_producto , "El nombre del producto no es el seleccionado"

          print(f"El producto comprado coincide con el que está en el carrito que es: {producto_comprado}")

    except Exception as e:
        print(f"Error en testa_login: {e}")
        raise
    finally:
         driver.quit()
#-----------------------------------------------------------------------------------------------
