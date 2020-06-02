import unittest
from tests import MyTestCase

# 創建一個測試套件
suite = unittest.TestSuite()

# 方式一：
# 添加測試用例 addTest(測試類(用例名))
# suite.addTest(MyTestCase('test_3'))
# suite.addTest(MyTestCase('test_5'))
# suite.addTest(MyTestCase('test_1'))

# 方式二：
# case = [
#     MyTestCase('test_3'), MyTestCase('test_5'), MyTestCase('test_2')
# ]
# suite.addTests(case)

# 方式三：
# 添加整個類進suite
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=MyTestCase))

# 方式四：
# 透過匹配的所有test.py檔，將其中的用例全部執行
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='*.py')

# 套件要透過Runner對象執行
runner = unittest.TextTestRunner()
runner.run(suite)
# runner.run(discover)





