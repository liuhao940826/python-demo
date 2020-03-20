# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
yamldict ={'path': {'tieba_config': '/Users/liuhao/PycharmProjects/self_tieba_spider2', 'weibo_config': '/Users/liuhao/PycharmProjects'}, 'time': {'interval': {'start_time': 180, 'end_time': 300}}, 'url': {'tieba_applyTask_url': 'http://localhost:9005/social-api/inner/channel/tiebaConfig/applyTask', 'weibo_applyTask_url': 'http://localhost:9005/social-api/inner/api/crm/weibo/collect/applyTask'}}

print(yamldict['path']['tieba_config'])

print("贴吧接口请求地址:{}".format(yamldict['url']['tieba_applyTask_url']))
print("贴吧接口请求地址:{}".format(type(yamldict['url']['tieba_applyTask_url'])))

# print('旧的dict:',dict)
# print(dict['Name'])
#
# # dict['Name']='新的值'
# dict.setdefault('Name','新的值default')
#
#
# print('新的dict:',dict)
#
# res =",".join(dict)
#
# print("res:{}".format(res))
#
#
#
#
# print("最后的str:{}".format(str))
#
# print("================================================")
#
# dict2={"dict":{}}
# print("dict2的类型:{}".format(type(dict2)))
# print("dict2中的dict的类型:{}".format(type(dict2['dict'])))
# dict2['dict']['新的内容'] = "是我是我"
#
# print("最后的dict2:{}".format(dict2))

class test2:

    def __init__(self):
        self.gender = 'male'


a = test2
a.isSend = True
# print(a.__dict__)

if a.isSend:
    print('true的时候出现')