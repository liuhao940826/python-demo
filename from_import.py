from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
# 因为已经导入path成员，所以此处引用时不需要加sys.path
print("因为已经导入path成员，所以此处引用时不需要加sys.path")
print('path:', path)