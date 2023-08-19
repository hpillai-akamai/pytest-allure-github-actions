import allure
import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

# Tests
@pytest.fixture
def calculator():
    return Calculator()

@allure.title("Addition Test")
def test_addition(calculator):
    with allure.step("Performing addition"):
        result = calculator.add(2, 3)
    assert result == 5

@allure.title("Subtraction Test")
def test_subtraction(calculator):
    with allure.step("Performing subtraction"):
        result = calculator.subtract(5, 3)
    assert result == 2

@allure.title("Multiplication Test")
def test_multiplication(calculator):
    with allure.step("Performing multiplication"):
        result = calculator.multiply(4, 3)
    assert result == 12

@allure.title("Division Test")
def test_division(calculator):
    with allure.step("Performing division"):
        result = calculator.divide(8, 2)
    assert result == 4
