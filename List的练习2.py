# List（列表） 是 Python 中使用最频繁的数据类型。
#
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
#
# 列表截取的语法格式如下
list = ['abcd', 786, 2.23, 'runoob', 70.2]

list2 = ['q', 'w', 'e', 'r', 't']


if 'abcd' not in list:
    print("进来")

print(list.__contains__('abcd'))


first = enumerate(list2)

print("first:{}".format(first))

#集合下标遍历
for i, value in enumerate(list):
    print("下标:{},值:{}".format(i, value))
    print("list2:{},值:{}".format(i,list2[i]))
