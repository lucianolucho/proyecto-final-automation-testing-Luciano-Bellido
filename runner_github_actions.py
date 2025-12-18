import pytest


pytest.main(["test/","--html=reports/report.html","--self-contained-html","-v"])