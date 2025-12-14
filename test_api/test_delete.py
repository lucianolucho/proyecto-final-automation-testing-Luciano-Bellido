import requests
import pytest

@pytest.mark.api
def test_delete_users(url_base,header_request):
  #  urlEndPoint = 'https://reqres.in/api/users/2'
    #encabezado = {"x-api-key": "reqres-free-v1"}
   # encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}

   # response = requests.delete(urlEndPoint,headers = encabezado)

    url_base = f"{url_base}/2"
    response = requests.delete(url_base, headers= header_request)

    #validaciones
    assert response.status_code == 204