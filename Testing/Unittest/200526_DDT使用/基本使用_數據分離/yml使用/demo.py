import yaml


with open('data.yml', 'r', encoding='utf-8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)


with open('data2.yml', 'r', encoding='utf-8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
