from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

import time
import pytest

#funcion de prueba para el navegacion de catalogo 

@pytest.mark.skip(reason="Clase ignorada")
def test_navegacion_catalogo(login_in_driver):  

    try:
        driver = login_in_driver
        catalogo = InventoryPage(driver)        

        #verificar la seccion del titulo 
        titulo = catalogo.obtener_titulo()
        print(f'el valor d ela variable es  {titulo}')
        assert titulo == 'Products', "el titulo no es el esperado"
        
        #contar productos visibles
        productos = catalogo.obtener_productos()
        print(f'Se encontraron {len(productos)} productos.')

        assert len(productos)> 0, "no se muestran productos "
        
        time.sleep(2)

        #Validar que elementos importantes de la interfaz estén presentes (menú,filtros, etc.)
        #valida la presencia del menú
        menu = catalogo.menuPresente() 
        assert menu.is_displayed() , "el menú no se esta mostrando"
        
        #valida lapresencia del filtro  
        filtro = catalogo.carritoPresente()  
        assert filtro.is_displayed() , "el carrito  no se esta mostrando"  
        

    except Exception as e:
        print(f"error en test_login:  {e}")
        raise
    finally:
         driver.quit()




     