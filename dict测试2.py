dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print('旧的dict:',dict)
print(dict['Name'])

# dict['Name']='新的值'
dict.setdefault('Name','新的值default')


print('新的dict:',dict)



