import requests
import pytest

@pytest.mark.api
def test_patch_users(url_base,header_request):
    #urlEndPoint = 'https://reqres.in/api/users/2'
    #encabezado = {"x-api-key": "reqres-free-v1"}
    #encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}

    data = {"name":"Luciano", "job":"Desarrollador"}

    #response = requests.patch(urlEndPoint, headers=encabezado, json = data) 

    url_base = f"{url_base}/2"
    response = requests.patch(url_base, headers= header_request, json = data) 

    # validacion de status code
    assert response.status_code == 200 
    
    #validacion de datos 
    body = response.json()

    assert body["name"] == data["name"]


