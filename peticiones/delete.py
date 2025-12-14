import requests
import pytest
 
urlEndPoint = 'https://reqres.in/api/users/2'

#encabezado = {"x-api-key": "reqres-free-v1"}

encabezado  = {"x-api-key": "reqres_32eba74ff27b4390a10d4ec7c60eec96"}

response = requests.delete(urlEndPoint, headers= encabezado)

print(response.status_code)
print(response.text)
