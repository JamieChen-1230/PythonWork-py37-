import pytest


def func(x):
    return x + 1


# 方法名為test_*
def test_zero():
    print('這試測試用-0')


def test_one():
    print('這試測試用-1')
    assert func(3) == 5


# 類名為Test*
class TestCase:
    # 方法名為test_*
    def test_two(self):
        assert 1 == 2  # 如果failed的話，後面的代碼就不會執行了
        print('這試測試用-2')

    def test_three(self):
        pytest.assume(1 == 2)  # 使用pytest.assume來定義assert的話，就算failed的話，後面的代碼還是會執行
        print('這試測試用-3')


if __name__ == '__main__':
    """
    原因是因為Pycharm會把一些信息自動記錄下來。
    如果遇到奇怪的問題可以去中上偏右有一個顯示你當前文檔的框框點下去 => Edit Configurations 
    => 把左半邊有關此文檔的紀錄都刪掉(用左上的-來刪除) => +一個python  => script path選擇此文檔路徑 => OK
    """
    # 在這邊調用命令行的參數
    pytest.main(['-v', '--reruns=2', '200510_sample_test.py::test_one'])
