import unittest
import yaml
import ddt


@ddt.ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print()

    # 會自動讀取json內的數據並導入
    @ddt.file_data('data3.yml')
    def test_1(self, **kwargs):
        print(kwargs.get('name'))
        print(kwargs.get('age'))
        print('**********************************')


if __name__ == '__main__':
    unittest.main()
