from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

from utils.logger import logger

import time
import pytest

#funcion de prueba para el login exitoso 

def test_login_validacion(login_in_driver,debe_funcionar= True):
   
    try:
       logger.info("Obtencion de driver")
       driver = login_in_driver
       LoginPage(driver).login_completo("standard_user","secret_sauce")
       #driver = login_in_driver.login_completo("standard_user","secret_sauce")
       
       #assert False
       print("****************** metodo: test_login_validacion ....**************************")
       if debe_funcionar == True:
            logger.info("Se verifica que el redireccionamiento sea exitoso") 
            assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
            logger.info("Login completado exitosamente")   
       elif debe_funcionar == False:
             mensaje_error = LoginPage(driver).obtener_error()
             assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"

    except Exception as e:
        print(f"error en test_login:  {e}")
        raise
    finally:
         driver.quit()