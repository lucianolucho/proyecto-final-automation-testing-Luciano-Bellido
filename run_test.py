import pytest

# Lista de archivos de prueba a ejecutar
test_files = [
    "test/test_login.py",
    "test/test_login_user_pass.py",
    "test/test_login_faker.py",
    "test/test_login_csv.py",
    "test/test_navegacion_catalogo.py",
    "test/test_carrito.py",
    "test/test_carrito_json.py",
    "test_api/test_api_reqres.py",
    "test_api/test_get.py",
    "test_api/test_post.py",
    "test_api/test_put.py",
    "test_api/test_patch.py",
    "test_api/test_delete.py"
]

# Argumentos para ejecutar las pruebas: Archivos + REPORT HTML
pytest_args = test_files + ["--html=reports/report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)