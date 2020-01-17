dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print('旧的dict:',dict)
print(dict['Name'])

# dict['Name']='新的值'
dict.setdefault('Name','新的值default')


print('新的dict:',dict)

res =",".join(dict)

print("res:{}".format(res))




print("最后的str:{}".format(str))

print("================================================")

dict2={"dict":{}}
print("dict2的类型:{}".format(type(dict2)))
print("dict2中的dict的类型:{}".format(type(dict2['dict'])))
dict2['dict']['新的内容'] = "是我是我"

print("最后的dict2:{}".format(dict2))






