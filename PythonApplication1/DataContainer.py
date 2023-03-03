name_list = ["zhangsan","lisi",666,"zhaoliu",12.34]
print(name_list)
print(type(name_list))

my_list = [["zhangsan",28,"Female"],["lisi",22,"Male"]] #嵌套列表
#print(my_list)
#print(type(my_list))
#print(my_list[0][0], end=' ')
#print(my_list[0][1], end=' ')
#print(my_list[0][2])
#print(my_list[1][0], end=' ')
#print(my_list[1][1], end=' ')
#print(my_list[1][2])
print(my_list[-1][-1])
print(my_list[-1][-3])
print(my_list[-2][-3])
print(my_list[-2][-1])

print(my_list[0].index("zhangsan"))
my_list[1][1] = 33
print(my_list)
my_list.insert(1,["wangwu",21,"Female"] )
print(my_list)
my_list.append(["zhaoliu",18,"Female"])
print(my_list)
my_list.extend([["Mary",22,"Female"],["Peter",15,"Male"]])
print(my_list)
del my_list[-1]
print(my_list)
my_list.pop(-1)
print(my_list)
my_list.insert(1,["zhaoliu",18,"Female"])
print(my_list)
#my_list.remove(["zhaoliu",18,"Female"])
print(my_list)
#my_list.clear()
#print(my_list)
print(my_list.count(["zhaoliu",18,"Female"]))
print(len(my_list))

#30.练习
#定义一个列表 内容是[21,25,22,25,33,22]
numlist = [21,25,22,25,33,22]
#追加一个数字31到列表尾部
numlist.append(31)
#取出第一个元素
print(numlist[0])
#取出最后一个元素
print(numlist[-1])
print(numlist[len(numlist)-1])
#查找元素33的位置
print(numlist.index(33))
print(numlist)


def list_while_func():
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

#list_while_func()

def list_for_func():
    for a in my_list:
        print(a)

list_for_func()

#32. 练习
#定义一个列表 [1,2,3,4,….10]
#使用while循环取出列表中偶数
#使用for循环取出列表中奇数

numlist = range(1,11)
index = 0
while index < len(numlist):
    if numlist[index] % 2 == 0:
        print(numlist[index])
    index += 1

for a in numlist:
    if a % 2 == 1:
        print(a)

# 27.元组
mytuple = tuple() #空元组 
mytuple = (["zhangsan",28,"Female"],["lisi",22,"Male"])
print(mytuple)
print(type(mytuple))
#定义单个元素的元组，末尾加逗号，不然就不是元组类型了
mytuple1 = (["zhangsan",28,"Female"],)
mytuple2 = (["zhangsan",28,"Female"])
print(mytuple1)
print(mytuple2)
print(type(mytuple1))
print(type(mytuple2))
mytuple = (("zhangsan",28,"Female"),("lisi",22,"Male"),("zhangsan",28,"Female"))
print(type(mytuple[0]))
print(mytuple[1][2])
print(f"myturple's length is {len(mytuple)}")
print(mytuple.count(("zhangsan",28,"Female")))
print(mytuple[2].index(28))

index = 0
while index < len(mytuple):
    print(mytuple[index])
    index += 1

for a in mytuple:
    print(f'tuple for {a}')

mytuple = (("zhangsan",28,"Female"),("lisi",22,"Male"),["zhangsan",28,"Female"])
#mytuple[0][0] = "wangwu"
mytuple[2][0] = "wangwu"
print(mytuple)

#34.练习
#定义一个元组 ('周杰伦'，40，['music','football'])，记录姓名，年龄，喜好
mytuple=('周杰伦', 40, ['music','football'])
#查询年龄所在下标位置
print(mytuple.index(40))
#查询学生所在姓名
print(mytuple[0])
#删除学生喜好“football”
del mytuple[2][1]
#增加学生喜好“coding”
mytuple[2].insert(1,'coding')
print(mytuple)

#35 字符串容器
str = "connie and connor"
print(str.index("and"))
print(str[-1])
str1 = str.replace("connor","connect")
print(f'"{str}" replace to "{str1}"')
str = "connie connor connect mary"
strlist = str.split(" ")
print(f'str.split()\'s return type is {type(strlist)} \n {strlist}')
str = "  connie and connor   "
print(f'String：{str} removed space is {str.strip()}.')
str = str.strip() + "nnoc"
print(f'String：{str} removed conn is {str.strip("conn")}.')
print(f'{str}:{str.count("conn")}:length:{len(str)}')

#36. 练习
#统计字符串内有多少指定字符串
str = "This is my family, they are Connor and Connect"
print(str.count("nn"))
#将字符串内空格全部替换为|
str = str.replace(" ","|")
#按照|分割，取得列表
strlist = str.split("|")
print(strlist)

# 37.序列切片
# 对list切片
seq = list(range(1, 21))
print(f'{type(seq[0:15:2])},content:{seq[0:15:2]}')
print(seq[:]) # 从头到尾切片，step = 1
# 对string切片
print(str)
print(f'{type(str[::2])},content:{str[::2]}')
print(f'{type(str[::-1])},content:{str[::-1]}')
print(f'{type(str[3:1:-1])},content:{str[3:1:-1]}')
# 对tuple切片
turple = (1,2,3,4,5)
print(f'{type(turple[::-2])},content:{turple[::-2]}')

#38.集合
myset = set()
myset = {1,2,1,5,8,9,3,4,5,5,5}
print(myset)
myset.add(10)
myset.add(5)
myset.remove(2)
print(myset)
print(myset.pop())
myset.clear()
print(myset)
myset1 = {1,2,3}
myset2 = {2,3,5}
print(myset1.difference(myset2))
print(myset1)
print(myset2)
myset1.difference_update(myset2)
print(myset1)
print(myset2)
myset3=myset1.union(myset2)
print(myset1)
print(myset2)
print(f'set3 is {myset3},set3 length is {len(myset3)}')

for element in myset3:
    print(element)


#39. 集合练习
#定义一个空集合
#通过for循环遍历列表
#在for循环中将列表的元素添加至集合
#最终得到去重后的集合对象，打印输出
myset = set()
print(my_list)
for element in my_list:
    myset.add(tuple(element))
print(f'myset without duplicates: {myset}')


#40. 字典
#定义空字典
#重复key字典
#从字典中基于key获取value
mydict = {}
mydict = dict()
mydict = {'connie': 100,'connor': 100,'connect': 0,'connect': 60}
print(mydict['connect'])
#定义嵌套字典
mydict = { 
    "12345": {'name': 'zhangsan','gender': 'Male','age': 18},
    "12346": {'name': 'lisi','gender': 'Female','age': 21},
    "12347": {'name': 'wangwu','gender': 'Male','age': 25},
    }
#从嵌套字典中获取数据
print(mydict)
print(mydict['12345']['name'])
print(mydict['12346']['name'])
print(mydict['12347']['name'])
mydict['12348'] = {'name': 'zhaoliu','gender': 'Female','age': 33}
mydict['12346'] = {'name': 'lisi','gender': 'Female','age': 22}
print(mydict)
mydict.pop('12346')
print(mydict)
print(f'keys" type:{type(mydict.keys())}, content:{mydict.keys()}')
for a in mydict.keys():
    print(f'{a}:{mydict[a]}')

for key in mydict:
    mydict[key]['grade'] = 1
    print(f'{key}:{mydict[key]}')

 #41. 练习 根据表格定义字典 给所有工作年限>=3的员工，涨薪水2000块，级别提升1级
	#员工编号	工作年限	薪水	部门	level
	#0001	2	10000	IT	2
	#0002	3	10000	IT	3
	#0003	5	50000	CEO	9
	#0004	4	20000	HR	5
mydict = dict()
mydict['0001']={'working years':2, 'salary':10000,'department':'IT', 'level':2}
mydict['0002']={'working years':3, 'salary':10000,'department':'IT', 'level':3}
mydict['0003']={'working years':4, 'salary':50000,'department':'CEO', 'level':9}
mydict['0004']={'working years':5, 'salary':20000,'department':'HR', 'level':5}
for key in mydict:
    if mydict[key]['working years'] >= 3:
        mydict[key]['salary'] += 2000
        mydict[key]['level'] += 1
print(mydict)

mytuple = (1,2,3,5,7,9,22)
print("--------------")
print(len(my_list))
print(len(mytuple))
print(len(str1))
print(len(myset))
print(len(mydict))
print("--------------")
print(max(my_list))
print(max(mytuple))
print(f'str1:{str1},max:[{max(str1)}]')
print(max(myset))
print(max(mydict))
print("---------------")
print(min(my_list))
print(min(mytuple))
print(f'str1:{str1},min:[{min(str1)}]')
print(min(myset))
print(min(mydict))
print(sorted(mytuple, reverse=True))
print(sorted(mydict, reverse=True))

