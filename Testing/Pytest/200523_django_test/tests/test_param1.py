import requests
import pytest
import allure


class TestParam1(object):

    def test_param_1(self):
        url = "http://127.0.0.1:8000/api/v1/users/"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        payload = {
            "name": "android",
            "age": 7,
            "height": 150,
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.json())
        assert response.json()["message"] == "Success"
