import requests
import time
import pytest

@pytest.mark.api
def test_putt_users(url_base,header_request):

    urlEndPoint = f"{url_base}/2"
    #encabezado = {"x-api-key": "reqres-free-v1"}
   # encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}

    data = {"name":"Luciano", "job":"Desarrollador"}

    
    inicio= time.time()
   # response = requests.put(urlEndPoint, headers=encabezado, json = data) 
    response = requests.put(urlEndPoint, headers=header_request, json = data) 
    tiempo_respuesta  = time.time() - inicio 


     #validacion de status 
    assert response.status_code == 200 

     #validacion de tiempo de respuesta
    assert tiempo_respuesta < 2 , f"la api tardó  demasiado: {tiempo_respuesta} "


    # chequeamos los datos   
    body = response.json()

    #chequeamos que el cuerpo se haya actualizado   
    assert "updatedAt" in body

    #se verifica que el contenido del campo sea un string
    assert isinstance(body["name"], str)    

    assert body["name"] == data["name"]
