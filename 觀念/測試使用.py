di = {
    'name': 'jamie',
    'age': 18
}


def di_print(name, age):
    print(name, age)


di_print(**di)  # **di => 參數會變成 name=jamie和age=18(要使用的話字典的key要與函數的參數名相同)
