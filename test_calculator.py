import allure
import pytest


@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.sanity
@pytest.mark.master
@pytest.mark.basic_sanity
def test_addition():
    allure.dynamic.suite("SUITE_1")
    print("addition of 2 and 3")
    assert 2+3 == 5

@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.master
@pytest.mark.basic_sanity
def test_subtraction():
    allure.dynamic.suite("SUITE_1")
    print("subtraction of 3 from 5")
    assert 5-3 == 2

@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.master
@pytest.mark.basic_sanity
def test_multiplication():
    allure.dynamic.suite("SUITE_1")
    print("Mulitply 4 and 3")
    assert 4*3 == 12

@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.master
def test_division():
    allure.dynamic.suite("SUITE_1")
    pirnt("Divide 8 by 2")
    assert 8/2 == 4

@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.basic_sanity
def test_failure():
    allure.dynamic.suite("SUITE_1")
    print("TC failure here")
    assert 3 == 4
