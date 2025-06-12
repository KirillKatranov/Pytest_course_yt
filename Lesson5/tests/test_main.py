#1. Можем несколько тестовых функций объединять в тестовый класс - удобно | pytest tests/test_main.py::TestCalculator::test_divide
#2. Контекстный менеджер with pytest.raises(TypeError) позволяет пройти тест если эта ошибка выбросилась
#3. Через дополнительный служебный параметр expectation мы можем параметризовать работу с ошибками, 
#   т.е. если в одном случае мы ожидаем ошибку и она происходит тест прошёл, а в другом мы не ожидаем ошибку 
#   её нет и тест тоже прошёл

from src.main import Calculator
import pytest
from contextlib import nullcontext as does_not_raise

class TestCalculator:
    @pytest.mark.parametrize(
            "a, b, res, expectation", #expectation - ожидание чего-то
            [
                (1, 2, 0.5, does_not_raise()),
                (5, 5, 1.0, does_not_raise()),
                (5, "5", 2, pytest.raises(TypeError)),
            ]
            )
    def test_divide(self,a, b, res, expectation):
        #with pytest.raises(TypeError):
        with expectation:
            assert Calculator().divide(a,b) == res

    def test_add(self):
        x = 1
        y = 2
        assert Calculator().add(x,y) == 3