#Вызов конкретного теста со всеми его кейсами pytest tests/test_main.py::test_divide
#Вызов конкретного теста с конкретным кейсом pytest tests/test_main.py::test_divide[1-2-0.5]
from src.main import Calculator
import pytest

@pytest.mark.parametrize(
        "a, b, res",
        [
            (1,2,0.5),
            (5,5,1.0),
            (5,5,2),
        ]
        )
def test_divide(a, b, res):
    assert Calculator().divide(a,b) == res

def test_add():
    x = 1
    y = 2
    assert Calculator().add(x,y) == 3