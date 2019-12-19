class test:
    name = 'alex'

    def run(self):
        pass


t = test()
'''
    获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选
    注意：name必须用“”引起来　　  方法拿到的是地址，加（）即可运行函数
'''

print(getattr(t, 'name'))  # alex
print(getattr(t, 'run'))  # <bound method test.run of <__main__.test object at 0x0121FFB0>>
print(getattr(t, 'age', 12))  # 12