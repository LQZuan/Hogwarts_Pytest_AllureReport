"""
完善你的Calc的用例，增加更多用例（浮点数相乘bug）
- 提交你的github测试文件地址
- 把allure的首页截图到回帖中
"""
import allure
import pytest

from core.Calc import Calc
from tests.base import Base


@allure.feature("除法测试用例")
class TestCalcDiv(Base):

    @allure.story("正常整数")
    @pytest.mark.parametrize("a, b, exp", [
        (1, 2, 0.5),
        (100, 10, 10),
        (-3, -4, 0.75),
        (-10, -5, 2),
        (250, -5, -50),
        (-60, 3, -20)
    ])
    def test_div_int(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("正常小数")
    @pytest.mark.parametrize("a, b, exp", [
        (1.5, 0.3, 5),
        (0.4, 0.8, 0.5),
        (-0.9, -0.3, 3),
        (-0.4, -1.6, 0.25),
        (2.8, -0.7, -4),
        (-5.6, 0.8, -7),
        (0.008, 0.2, 0.04)
    ])
    def test_div_float(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("正常小数和整数")
    @pytest.mark.parametrize("a, b, exp", [
        (5, 0.5, 10),
        (1.8, 6, 0.3),
        (-0.6, -3, 0.2),
        (-3, -0.5, 6),
        (4, -0.2, -20),
        (-1.5, 3, -0.5)
    ])
    def test_div_mix(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("特殊值0处理")
    @pytest.mark.parametrize("a, b, exp", [
        (0, 100, 0),
        (0, -10, 0),
        (0, 0.9, 0),
        (0, -1.784, 0)
    ])
    def test_div_zero(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("错误类型")
    @pytest.mark.parametrize("a, b", [
        (2, 0),
        (-102, 0),
        (0, 0),
        (1.85, 0),
        (-0.09, 0),
        ('jjj', 'hhh'),
        ('*', ','),
        (True, False)
    ])
    def test_div_err(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)


@allure.feature("乘法测试用例")
class TestCalcMul:

    @allure.story("正常整数和0")
    @pytest.mark.parametrize("a, b, exp", [
        (1, 2, 2),
        (100, 10, 1000),
        (-3, -4, 12),
        (-10, -5, 50),
        (250, -5, -1250),
        (-60, 3, -180),
        (0, 0, 0),
        (0, 13, 0),
        (294, 0, 0),
        (-293, 0, 0),
        (0, -39, 0)
    ])
    def test_mul(self, a, b, exp):
        assert self.calc.mul(a, b) == exp

    @allure.story("正常小数")
    @pytest.mark.parametrize("a, b, exp", [
        (1.5, 0.3, 5),
        (0.4, 0.8, 0.5),
        (-0.9, -0.3, 3),
        (-0.4, -1.6, 0.25),
        (2.8, -0.7, -4),
        (-5.6, 0.8, -7),
        (0.008, 0.2, 0.04)
    ])
    def test_mul_float(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("正常小数和整数")
    @pytest.mark.parametrize("a, b, exp", [
        (5, 0.5, 10),
        (1.8, 6, 0.3),
        (-0.6, -3, 0.2),
        (-3, -0.5, 6),
        (4, -0.2, -20),
        (-1.5, 3, -0.5),
        (958.039, 0, 0),
        (0, 0.001, 0),
        (-0.394, 0, 0),
        (0, -9.39244, 0)
    ])
    def test_mul_mix(self, a, b, exp):
        assert self.calc.div(a, b) == exp

    @allure.story("错误类型")
    @pytest.mark.parametrize("a, b", [
        ('jjj', 'hhh'),
        ('*', ','),
        (True, False)
    ])
    def test_div_err(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)


@allure.feature("混合场景,流程示例")
class TestCalcMix:

    @allure.story("先除后乘")
    def test_mix1(self):
        result1 = self.calc.div(1024, 128)
        result2 = self.calc.mul(16, 16)
        assert result1 == 8
        assert result2 == 256

    @allure.story("先乘后除")
    def test_mix2(self):
        result1 = self.calc.mul(1024, 1024)
        result2 = self.calc.div(32, 8)
        assert result1 == 1048576
        assert result2 == 4

