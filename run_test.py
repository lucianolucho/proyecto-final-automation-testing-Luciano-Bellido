import pytest

# Lista de archivos de prueba a ejecutar
test_files = [
    "test/test_login.py",
    "test/test_navegacion_catalogo.py",
    "test/test_carrito.py",
    "test_api/test_api_reqres.py"
]

# Argumentos para ejecutar las pruebas: Archivos + REPORT HTML
pytest_args = test_files + ["--html=reports/report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)