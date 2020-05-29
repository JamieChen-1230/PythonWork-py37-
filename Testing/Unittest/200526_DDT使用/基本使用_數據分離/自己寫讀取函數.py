import unittest
import ddt


def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for line in f.readlines():
            print(line)
            data.append(line.replace('\n', '').split(','))
            print(data)
        return data


# 測試用例類(必須繼承Unuttest TestCase類)
@ddt.ddt  # 要在用例中使用ddt，需要先在測試類上導入ddt(@ddt.ddt)
class MyTestCase(unittest.TestCase):

    @ddt.data(*read_data('data.txt'))
    @ddt.unpack  # 當用例參數不只一個時須使用，unpack用於拆包
    def test_a(self, x, y):
        print(x, y)


if __name__ == '__main__':
    unittest.main()
