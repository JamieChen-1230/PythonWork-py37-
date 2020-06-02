import unittest
from tests import MyTestCase
import HTMLTestRunner
import os

# 創建一個測試套件
suite = unittest.TestSuite()

report_path = './report/'
report_file = report_path + 'report.html'
if not os.path.exists(report_path):
    # 如果沒有report文件夾則創建
    os.mkdir(report_path)

report_title = '測試報告初試'
report_description = '第一次使用HTMLTestRunner生成測試報告'
# 需使用wb模式寫入
with open(report_file, 'wb') as f:
    # 添加測試用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=MyTestCase))
    # 使用HTMLTestRunner建立測試報告
    # stream：欲寫入的文件, title：標題, description：描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=report_title, description=report_description)
    runner.run(suite)




