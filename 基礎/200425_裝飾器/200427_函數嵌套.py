"""
嵌套函數：函數裡面在去定義一個函數，這就是嵌套函數。
"""


def father(name):
    print("from father %s" % name)  # => from father jamie

    def son():  # 函數即變量
        print(name)  # => jamie

        def grandson():
            name = "sb"
            print(name)  # => sb
        grandson()
    print(locals())  # => {'name': 'jamie', 'son': <function father.<locals>.son at 0x0000022C899E5510>}，顯示局部變量
    son()


father("jamie")

