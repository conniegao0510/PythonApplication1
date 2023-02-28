#money = 50
#ice = 10

#print("money:",money-ice)

#print(type(13.14))
#print(type(13))
#print(type("asdfasd"))
#print(type(money))

#print(int(11.3))
#print("11//2",11//2)
#print("2**4",2**4)
#print("9%2",9%2)

#tel = 12345
#message = "my tel number is %s" % tel
#print(message)

#tel = 12345
#age = 18
#message = "my tel number is %s, I am %s years old." % (tel, age)
#print(message)

#print ("Please tell me who are you?")
#name=input()
#print ("Please tell me how old are you?")
#age=input()
#print("Helle %s, you are %s years old " % (name,age) )
#print (type(age))

#age = int(input("Please tell me who are you?"))
#if age < 18:
#    print("未成年")
#elif age >= 18 and age <= 25:
#    print("真年轻~")
#else:
#    print("老帮瓜！")

#import random
#guessnum = random.randint(1,100)
#yournum = 0
#count = 1
#def guessNum(flag,count):
#    if(flag > 0):
#        yournum = int(input ("your number is too big,guess again\n"))
#    elif(flag<0):
#        yournum = int(input ("your number is too small,guess again\n"))
#    else:
#        print ("Win, your number is correct. Your have guess %d times" % count)
#        return
#    count += 1
#    guessNum(yournum - guessnum,count)

#print("Welcome to Guess Number, what is your number?")
#yournum=int(input())
#guessNum(yournum - guessnum,count)


#import random
#guessnum = random.randint(1,100)
#count = 1
#print("Welcome to Guess Number, what is your number?")
#yournum = int(input())
#flag = yournum - guessnum
#while(flag != 0):
#    if flag > 0:
#        yournum = int(input ("your number is too big,guess again\n"))
#    else:
#        yournum = int(input ("your number is too small,guess again\n"))
#    count += 1
#    flag = yournum - guessnum
#print ("Win, your number is correct. Your have guessed %d times" % count)




#i=0
#sum = 0
#while i < 100:
#    i += 1
#    sum += i
#print(sum)

# 判断嵌套
#if int(input("what's your height?")) > 120:
#    print("Sorry, it is free under the 120 cm only!")
#    if int(input("what's your vip level?")) > 3:
#        print("free charge, congraulations!")
#    else:
#        print("not free, sorry")
#else:
#    print("welcome children")

#i = 0
#while i < 100:
#    print ("肖战，我爱你！")
#    i += 1


#i = 1
#while (i <= 100):
#    print("No. %d day" % i)
#    j = 1
#    while (j <= 10):
#        print("Send rose No.%d" %j)
#        j += 1
#    i += 1
#print("I love you, success!")

#i = 1
#j = 1
#while (i < 10):
#    while (j < 10):
#        if(i >= j):
#            print(f"{j} * {i} = {j * i}\t", end = ' ')
#        j += 1
#    print("")
#    i += 1
#    j = 1
 
#name = input("input your test string:")
#count = 0
#for x in name:
#    if x=='a':
#        count += 1
#print(f"you have inputed {count} letter 'a'~")

#count = 1
#for x in range(0, 100, 2):
#    count += 1
#print("oven number count ： %d" %count)

#for x in range(5):
#    print (x)
#print(x)

#for i in range(1,101):
#    print("Day:%d" %i)
#    for j in range(1,11):
#        print("No.%d rose" %j)
#print("success!")

#for i in range(1,10):
#    for j in range(1,i+1):
#        print(f"{j}*{i}={i*j}\t",end='')
#    print("")

#for x in range(1, 6):
#    print("statement1")
#    for y in range(1, 6):
#        print("statement2 ",end='')
#        continue
#        #break
#        print("statement3")
#    print("statement4")

#salary = 10000
#for i in range(1,2100):
#    if (salary > 0):
#        import random
#        score = random.randint(1,10)
#        if (score < 5):
#            print(f"Sorry, your score is {score} below 5, get salary next month")
#        else:
#            salary -= 1000
#            print(f"staff {i} got salary 1000, and there were {salary} remain")
#            continue    
#    else:
#        print("salary is empty, pelase get salary next month")
#        break

"""
函数说明
：param a: 形参a的说明
：param b: 形参b的说明
：return： 返回值的说明
"""
#def my_len(data):
#    count = 0
#    for x in data:
#        count += 1
#    print(f"data's length is {count}'")

#my_len(input("Str1\n"))
#my_len(input("Str2\n"))
#my_len(input("Str3\n"))

#num = 200
#def fun_a():
#   global num
#   num = 500
#fun_a()
#print(num)


"""
演示银行存取案例开发
"""

# define global variable money name
money = 5000000
name = None

# require user input the name
name = input ("Please input your name:")

# define search function
def query(show_header):
    if show_header:
        print("---------------Balance-----------------")
    print(f"Hello, your balance:{money}")

# define save money function
def savingmoney(num):
    print("---------------Saving-----------------")
    global money
    money += num
    print(f"Hello, you have saved {num} successfully")
    query(False)

# define take money function
def getmoney(num):
    global money
    money -= num
    print("---------------Getting-----------------")
    print(f"Hello, you have take {num} successfully")
    query(False)
# define menu function
def main():
    print("---------------MainMenu-----------------")
    print(f"Hello,{name} Welcome to my bank, please choose the operation as below")
    print("query\tinput 1")
    print("save\tinput 2")
    print("take\tinput 3")
    print("exit\tinput 4")
    return input("Please input your choose")
    
# define the loop , the application will not stop 
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = input("How much money you want to save?")
        savingmoney(int(num))
        continue
    elif keyboard_input == "3":
        num = input("How much money you want to take?")
        getmoney(int(num))
        continue
    else:
        print("Exit the system....")
        break