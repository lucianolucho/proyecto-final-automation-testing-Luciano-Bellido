import pytest


pytest.main(["test/", "test_api/","--html=reports/report.html","--self-contained-html","-v"])