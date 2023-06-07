# 1.返回多个返回值
def return_test():
    return "Connie",1986,5
x, y, z = return_test()
print(f"x, y, z: {x},{y},{z},return type:{type(return_test())}")

# 2.多个参数传递
# 位置参数
def variables_fun(id,campus,name):
    print(f'You are in : {campus}, welcome, {name}')
variables_fun(12345,"HQ","Connie")
# 关键字参数
variables_fun(campus="HQ", name="Connie", id=12345) 
variables_fun(12345, name="Connie", campus="HQ") # 混用
# 缺省参数
def default_fun(campus = 'HQ'):
    print(f'your are in {campus} campus.')
default_fun()
# 位置型不定长参数
def var_fun(*args):
    print(args)
var_fun(1,2,3,"aa","cc")
# 关键字不定长参数
def var_fun(**args):
    print(f'type:{type(args)}:content:{args}')
var_fun(campus="HQ",name="可乐",grade=8)

# 3.匿名函数
def test_func(compute):
    result = compute(2,63)
    print(f'variable type: {type(compute)},{result}')

def compute(x, y):
    return x ** y

test_func(compute)

# 4.lambda 匿名函数
test_func(lambda x, y:x ** y)

# 6.文件处理
f = open('Resource/file.txt','r',encoding="UTF-8")
print(f'type:{type(f)}')
print(f'Read 10 chars:{f.read(10)}')
#print(f'Read all chars:{f.read()}')
print("------------------------------")
line1 = f.readline()
print(f'type: {type(line1)} , NO1 Line: {line1}')
line2 = f.readline()
print(f'type: {type(line2)} , NO2 Line: {line2}')
content = f.readlines()
print(f'Read Lines type: {type(content)} :typeReadlines:{content}')
f.close()
#For 循环读取文件
f = open('Resource/file.txt','r',encoding="UTF-8")
for line in f:
    print(f'type:{type(line)}:{line}')
f.close()
# with open 可以在操作完成之后自动关闭文件，避免遗忘关闭文件
with open('Resource/file.txt','r',encoding="UTF-8") as f:
    line = f.readlines()
    print(f'withopen:------------------------\n type:{type(line)},{line}')

# 7.练习统计文本文件种出现某字符的个数
# 方法一：read（）返回字符串
# 方法二：readline() 返回一行行，用空格切分的数组
with open('Resource/file.txt','r',encoding="UTF-8") as f:
    #print(f'人生的个数：{f.read().count("人生")}')
    count = 0
    for line in f:
        line = line.strip() #去除开头和结尾的空格和换行符
        words = line.split(" ")
        print(f'with open linetype:{type(line)},{line}----words type:{type(words)}-----{words}\n')
        for word in words:
            print (f'word type : {type(word)},{word}')
            c = word.count("人生")
            if c > 0:
                count += c
        
    print(f'word "人生" occurs:{count}')

# 8.文件写入
import time
with open('Resource/file1.txt','w',encoding="UTF-8") as f:
    f.write('Hello World')
    #time.sleep(600000) #运行到这里看一下文件内容，由此判断是否将内容写入内存缓冲区，open的文件不存在的话，会自动创建一个
    #f.flush() # f.close()方法内置了flush方法

with open('Resource/file2.txt','a',encoding="UTF-8") as f:
    f.write('Hello, Connie!')

with open('Resource/file2.txt','a',encoding="UTF-8") as f:
    f.write('\nWelcome to SCIS!')


# 9.文件处理综合案例 备份文件
# 备份2023文件夹下面的bill.txt中的正式记录，测试记录丢弃
with open('Resource/bill.txt','r',encoding="UTF-8") as f, open('Resource/bill.txt.bak','w',encoding="UTF-8") as f1:
    for line in f:
        line = line.strip()
        if(line.split(",")[-1] == "test"):
            continue      
        f1.write(line)
        f1.write("\n")

# 10.异常处理
##try:
##    f = open('linux.txt','r',encoding="UTF-8")
##except:
##    print(f'File not Found Error')
##    f = open('linux.txt','w',encoding="UTF-8")
        
# 捕获指定的异常
try:
##    print(name)
##    1 / 0
    print(1)
except (NameError, ZeroDivisionError) as e:
    print("Variable has not been defined.")
else:
    print("There is no exception!")
finally:
    print("Finally statement")

# 11.异常的传递
def func01():
    print("begin with func01")
    num = 1 / 0
    print("end with func01")

def func02():
    print("begin with func02")
    func01()
    print("end with func02")

def main():
    try:
        func02()
    except Exception as e:
        print(e)
main()

# 12.导包
import time
print("a")
time.sleep(5)
print("b")

import time as tt
print("a")
tt.sleep(5)
print("b")

# 13.自定义模块
import myModule
myModule.test(2,5)

# 导入同名包的情况，后面导入的覆盖前面的
from myModule1 import my_test
from myModule2 import my_test
my_test(5,3)

from myModule3 import *
from myModule3 import test
testA(2, 2)
testB(2, 2)
test(2, 2)

# 14.导入自定义模块
#import my_package.package_model1
#my_package.package_model1.mypack_m1(5,18)

#from my_package import package_model1
#package_model1.mypack_m1(5,18)

from my_package import *
package_model1.mypack_m1(5,18)
package_model2.mypack_m2(5,18)