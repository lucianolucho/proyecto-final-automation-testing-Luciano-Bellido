import requests
import pytest
 
urlEndPoint = 'https://reqres.in/api/users?page=2'

#encabezado = {"x-api-key": "reqres-free-v1"}
encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}


#def test_get_users():
response = requests.get(urlEndPoint, headers=encabezado, verify= False) #verify indica verifica o no certificado
print(response.status_code)
print(response.json())

data = response.json()

