# -*- coding: utf-8 -*-
# By: @ZhuNian
# Data: 2020.3.7 - 2020.3.8


#python里的组：列表(list)、元组(tuple), (元组的元素不能修改，列表的元素可以修改。)


'''列表'''

a=[1,2,3,4,5,6]
b=["hello",'abc',a,1]  #嵌套列表
c=[[1,2],[2,3],[True,False]]  #二位数组
d=[1,2,3]
print(a)
print(b)
print(c)
#输出指定列表中的元素
print(a[1])
print(a[2:4])
#列表的相加与相乘
print(a*2)
print(a+a)


print("\n")


'''元组'''
'''
  注意：当元组内只有一个元素时，其类型单个元素对应的类型。
  如（1）为int，（‘asd’）为str。
  而当列表内只有一个元素时，仍然是list类型。
'''
print((1,2,3))
#ord() 转换asc码  ord('d')


print("\n")

'''集合'''
#set 表示集合类型
a={1,2,3}
b={1,2,3,4,4,4,4,5}

print(a)
print(b)  #集合中不能有重复的数
print(type(a))
print(len(a))
#判断一个元素是否在这个集合中
print(1 in a)
print(1 not in a)
print({1,2,3,4,5,6}-{1,2,3})#求两个集合的差集
print({1,2,3,4,5,6}&{1,2,3})#求两个集合的交集
print({1,2,3,4,5,6}|{3,4,7})#求两个集合的并集
#空的集合 set()
print(type(set()))
print(type({}))

print("\n")


'''字典'''
#字典中有很多个key 和 value，不是集合和元组
#{key1: value1 ,key2:value2,.......}
#字典中不能有重读的key值,后面的key会覆盖前面的key值 b={'A':'苹果','A':'蚂蚁','B':'香蕉','O':'橙子'}
a={1:1,2:2,3:3}
print(type(a))
b={1:'我','A':'苹果','B':'香蕉','O':'橙子'}
print(b[1],b['A'])
#字典中：
#value 为: str int float list set dict
#key为: 要为不可变的类型 b={【1，2】:'我','A':'苹果','B':'香蕉','O':'橙子'}
#空的字典 ：{}

