innerlist = [123, 'runoob']


for item in innerlist:
    print("每一项的内容:",item)



outerlist = ['abcd', 786, 2.23, innerlist,'runoob', 70.2,["另一个内部数组",9999]]

for each in outerlist:
    if isinstance(each,list):
        for inner_each in each:
            print("内部嵌套的每一项:",inner_each)
    else:
        print("外部的每一项:",each)


