import allure
import pytest
import yaml

from tests.base import Base


class TestCalcDiv(Base):

    @allure.story("正常整数")
    @pytest.mark.parametrize("a, b, exp", yaml.safe_load(open("./data.yaml")))
    def test_div_int(self, a, b, exp):
        assert self.calc.div(a, b) == exp
