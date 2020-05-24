import os
import json


def get_data_path(case_path):
    # os.sep 代表\或/，系統會根據windows或linux來選擇
    file_path_list = os.path.dirname(case_path).split(os.sep + 'tests' + os.sep)
    # print(file_path_list)
    test_data_path = os.sep.join([file_path_list[0], 'data', file_path_list[1], os.path.basename(case_path).replace('.py', '.json')])
    # print(test_data_path)
    return test_data_path


def get_test_data(test_data_path):
    case = []
    payload = []
    with open(test_data_path, encoding='utf-8') as f:
        test_data = json.loads(f.read())
        test = test_data['test']
        for item in test:
            case.append(item['case'])
            payload.append(item.get('payload', {}))
    list_parameters = list(zip(case, payload))
    return case, list_parameters


if __name__ == '__main__':
    print(get_data_path(r'D:\Programming\WorkPlace\PythonWork(py37)\Testing\Pytest\200523_django_test\tests\test_param_splite\test_param_splite.py'))
