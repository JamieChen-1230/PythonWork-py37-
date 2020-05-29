import unittest
import yaml
import ddt


@ddt.ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print()

    # 會自動讀取json內的數據並導入
    # @ddt.file_data('data.json')
    # def test_1(self, name, age):
    #     print(name)
    #     print(age)
    #     print('**********************************')

    # (較優)因為不需要把每一個參數都一一設定
    @ddt.file_data('data.json')
    def test_1(self, **kwargs):
        print(kwargs.get('name'))
        print(kwargs.get('age'))
        print('**********************************')

    @ddt.file_data('data2.json')
    def test_2(self, txt):
        print(txt)
        print('**********************************')


if __name__ == '__main__':
    unittest.main()
