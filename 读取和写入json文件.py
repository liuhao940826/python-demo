import json
import os
import time


class Person:
    age =0

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        return "Person\n name: %s \t sex: %s " % (
         self.name, self.sex)


'''
json.load()从文件中读取json字符串

json.loads()将json字符串转换为字典类型

json.dumps()将python中的字典类型转换为字符串类型

json.dump()将json格式字符串写到文件中
'''
print("文件是否存在1",os.path.exists('config.json'))
print("文件是否存在2",os.path.exists('config.json2'))

# with open("config.json", 'r+') as load_f:
#     load_dict = json.load(load_f)
# print("读取到的json内容:",load_dict)
# print("=====================================")
# user_id_list = load_dict['user_id_list']
# print("user_id_list的集合内容:",user_id_list)
# print("var1的类型===",isinstance(user_id_list,list))


person =Person('刘浩','男')
person2 = Person('未知','女')

print("实例的str方法:",person.__str__())


personDict =person.__dict__
print("person的字典项:",personDict)
print("实例转字典项以后的json内容:",json.dumps(personDict))



print("=========================================")

dict ={'user_id_list': ['quotes-1006051672785037.txt', 'quotes-2815543444-1577083938.7455082.txt'], 'filter': 1, 'since_date': '2019-12-23', 'write_mode': ['csv'], 'mysql_config': {'host': 'host', 'port': 3306, 'user': 'root', 'password': '123456', 'charset': 'utf8mb4'}}

print("直接创建的字典项",dict)

user_id_list=dict['user_id_list']
user_id_list.append('quotes-2815543444-1577083938.7455082.txt')
print("拼接后的的字典项",dict)

# innerlist = ["1234212321", 'runoob']
#
# user_id_list.extend(innerlist)
#
# print("user_id_list的集合内容:",user_id_list)
#
with open("config.json", "w") as dump_f:
    json.dump(dict, dump_f)