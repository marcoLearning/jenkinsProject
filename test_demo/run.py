# coding=gbk
import os
import pytest

# pytest.main([])
os.system("pytest ./cases/test_pytest1.py")
os.system("allure generate ./allure_data -o ./allure_report --clean")