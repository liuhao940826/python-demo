import json

content = '{"name":"anthony","sex":"man"}'

print(content)

j=json.loads(content)

print("json.loads将字符串转为Python对象: type(json.loads(s)) = {}".format(type(json.loads(content))))
print("json.loads将字符串转为Python对象: json.loads(s) = {}".format(j))

name =getattr(j,"name","default")

print("能不能从json 中获取到数据 ","default"==name)








