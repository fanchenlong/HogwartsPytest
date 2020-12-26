import pytest
class Test_Demo:
    #pytest.mark.标签的名字（随便起）
    @pytest.mark.smoke
    def test_one(self):
        assert 1 == 1

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_two(self):
        assert 1 == 1