#Урок1 
from src.main import A

def test():
    assert 1 == 1

def test2():
    assert 2 == 2

def test_class_A():
    assert A.x == 1

#pytest или pytest -V для детального отображения тестов