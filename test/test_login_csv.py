from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.datos import leer_csv_login

import time
import pytest



#funcion de prueba para el login exitoso 
@pytest.mark.skip(reason="Clase ignorada")
@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_csv_login("datos/login.csv"))
def test_login_csv_validacion(login_in_driver_csv, usuario, password, debe_funcionar):
   
    try:
       driver = login_in_driver_csv
       
       print("****************** metodo: test_login_csv_validacion ....**************************")
       
      
       if debe_funcionar == True:
              assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
       elif debe_funcionar == False:
             mensaje_error = LoginPage(driver).obtener_error()
             print(mensaje_error)
             assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"

    except Exception as e:
        print(f"error en test_login:  {e}")
        raise
    finally:
         driver.quit()