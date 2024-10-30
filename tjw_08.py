a = int(input("请输入一个开始值:"))
b = int(input("请输入一个结束值："))
if a>=b-1 :
    print("输入值有误，请重新输入")
else:
    for i in range(a+1,b) :
        print("%d"%(i))