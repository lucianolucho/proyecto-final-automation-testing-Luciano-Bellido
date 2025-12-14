import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


import pathlib

target = pathlib.Path("reports/screems")

target.mkdir(parents= True, exist_ok= True)


@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # Para CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--incognito")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    time.sleep(1)
    # Para ver el resultado final
    driver.quit()


@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir().login_completo("standard_user","secret_sauce")
    return driver


@pytest.fixture
def login_in_driver_usuario_password(driver,usuario,password):
    LoginPage(driver).abrir().login_completo(usuario,password)
    return driver

@pytest.fixture
def login_in_driver_csv(driver,usuario,password):
    LoginPage(driver).abrir().login_completo(usuario,password)
    return driver
    
@pytest.fixture
def login_in_driver_json(driver,usuario,password):
    LoginPage(driver).abrir().login_completo(usuario,password)
    return driver   
    
@pytest.fixture
def login_in_driver_faker(driver,usuario,password):
    LoginPage(driver).abrir().login_completo(usuario,password)
    return driver    

#-------------------------------------------------------------------------------------------
# seccion api
@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    #return {"x-api-key": "reqres-free-v1"}
    return {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}   

#-------------------------------------------------------------------------------------------
# seccion captura pantalla
@pytest.hookimpl(hookwrapper=True)
# item : es el nombre del test
# call: la ejecución interna del test
def pytest_runtest_makereport(item, call):
    outcome = yield 

    report = outcome.get_result()

# el test se realiza en tres etapas:
##  setup
#    call 
#    teardown
    if report.when in ("setup","call") and report.failed:

        driver = item.funcargs.get("driver",None)
        
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            file_name= target / f"{report.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(str(file_name))