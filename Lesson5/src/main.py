from typing import Union
class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x / y
    
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y
    

if __name__ == "__main__":
    calculator = Calculator()
    
    print(1 == 1.0)