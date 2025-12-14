import requests
import pytest

@pytest.mark.api
def test_post_users(url_base,header_request):
  #  urlEndPoint = 'https://reqres.in/api/users'
    #encabezado = {"x-api-key": "reqres-free-v1"}
   # encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}

    # cuerpo en el post se suele llamar "payload
    payload =  {"name":"Luciano", "job":"Desarrollador"}  
    
   # response = requests.post(url_base, headers = header_request, json = payload)

    response = requests.post(url_base, headers = header_request, json = payload)
    

    # verificar que el recurso se haya creado 

    assert response.status_code == 201 

    data = response.json()
    
    # verificar que elnombre de la respuesta sea el mismo que el enviado

    assert  data["name"]  ==  payload["name"]
