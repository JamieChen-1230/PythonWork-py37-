import pytest
import requests


param = [
    ({'Content-Type': 'application/x-www-form-urlencoded'},
     {'name': 'android11', 'age': 9, 'height': 160}),
    ({'Content-Type': 'application/x-www-form-urlencoded'},
     {'name': 'android12', 'age': 10, 'height': 161}),
    ({'Content-Type': 'application/x-www-form-urlencoded'},
     {'name': 'android13', 'age': 11, 'height': 162})
]


class TestParam2(object):
    # param為要傳的數據，而其中的格式為[(headers, payload), (headers, payload), ...]
    @pytest.mark.parametrize("headers, payload", param)
    def test_param_2(self, headers, payload):   # headers和payload也要寫成參數傳進來
        url = "http://127.0.0.1:8000/api/v1/users/"
        # 發post請求
        print(payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        assert response.json()["message"] == "Success"  # 判斷是否成功
