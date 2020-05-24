import pytest
import requests

from utils.get_data import get_data_path
from utils.get_data import get_test_data

print(__file__)  # 獲取檔案路徑
case, param = get_test_data(get_data_path(__file__))
print(param)


class TestParam2(object):
    # param為要傳的數據，而其中的格式為[(headers, payload), (headers, payload), ...]
    @pytest.mark.parametrize("case, payload", param, ids=case)  # ids可以讓我們在測試結果中更好閱讀
    def test_param_2(self, case, payload):   # headers和payload也要寫成參數傳進來
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "http://127.0.0.1:8000/api/v1/users/"
        # 發post請求
        print(payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        assert response.json()["message"] == "Success"  # 判斷是否成功
