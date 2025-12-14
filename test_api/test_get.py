import requests
import pytest

@pytest.mark.api
def test_get_users(url_base,header_request):
   #urlEndPoint = 'https://reqres.in/api/users?page=2'
   # #encabezado = {"x-api-key": "reqres-free-v1"}
   # encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}


   # response = requests.get(urlEndPoint, headers = encabezado)

    url_base = f"{url_base}/2"
    response = requests.get(url_base, headers= header_request)
    
    #Verificar que la respuesta sea exitosa
    assert response.status_code == 200 
    
    #Verificar que tenga el cuerpo DATA
    data = response.json()
    assert "data"  in data

    #verificar que data es un a lista
   # assert isinstance(data["data"],list)  

    #verificar que la lista de datos sea mayor que uno 
    assert len(data["data"]) >  0      

    print(response.status_code)
    data = response.json()
    print(data)

 
   


