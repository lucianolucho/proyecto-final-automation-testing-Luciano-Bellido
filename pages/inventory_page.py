from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
   # _TITLE = (By.CLASS_NAME, "title")
    _TITLE = (By.CSS_SELECTOR, 'div .header_secondary_container .title')
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")


    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    #_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_BADGE = (By.CSS_SELECTOR, "#shopping_cart_container")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("entra en la clase InventoryPage")


    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        """Obtiene la lista de productos disponibles."""
        return self.driver.find_elements(*self._PRODUCTS)

    def agregar_primer_producto(self):
        """Añade el primer producto disponible al carrito."""
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self
    

    def seleccionarProductoByIndice(self, indice):
        productos = self.obtener_productos()
        nombre_producto = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name ').text
        productos[0].find_element(By.TAG_NAME, 'button').click()

        return  nombre_producto
     
     #Añadir un producto al carrito haciendo clic en el botón correspondiente
     #     nombre_producto = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name ').text
    #      productos[0].find_element(By.TAG_NAME, 'button').click()
          
          #nombre_producto =  catalogo.obtenerNombreProductoByIndice(driver, 0)
         # nombre_producto =  catalogo.seleccionarProductoByIndice(driver,0)

    def obtener_contador_carrito(self):
        """Obtiene el número de productos en el carrito."""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0


    def ir_al_carrito(self):
         """Navega a la página del carrito."""
         self.driver.find_element(*self._CART_LINK).click()
         # Importación lazy para evitar dependencias circulares

         from pages.cart_page import CartPage
         return CartPage(self.driver)


    def hacer_logout(self):
        """Cierra la sesión del usuario."""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    def menuPresente(self):
        '''Verifica navegacion del menu hamburguesa'''
        return self.driver.find_element(*self._MENU_BUTTON)
    
    def carritoPresente(self):
        '''Verifica navegacion del carrito'''
        return self.driver.find_element(*self._CART_BADGE)