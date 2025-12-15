from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

import time
import pytest

CASOS_LOGIN = [
("standard_user", "secret_sauce", True),# usuario válido, login exitoso
("locked_out_user", "secret_sauce", False), # usuario bloqueado, login falla
("usuario_malo","password_malo",False) #credenciales clave,debe_funcionar", inválidas, login falla
]

#funcion de prueba para el login exitoso 
#@pytest.mark.skip(reason="Clase ignorada")
@pytest.mark.parametrize("usuario, password,debe_funcionar",CASOS_LOGIN)
def test_login_user_pass_validacion(login_in_driver_usuario_password, usuario, password, debe_funcionar):
   
    try:
       driver = login_in_driver_usuario_password
       LoginPage(driver).login_completo(usuario,password)
      # driver = login_in_driver_usuario_password.login_completo(usuario,password)
       
       print("****************** metodo: test_login_user_pass_validacion ....**************************")
       
      
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