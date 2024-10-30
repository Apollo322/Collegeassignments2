import sys

a = int(input("请输入一个季度数值："))
if a<1 or a>4 :
    print("输入错误，重新输入")
    sys.exit()
else :
    if a == 1 :
        print("该季度有3,4,5月份")
    elif a == 2 :
        print("该季度有6,7,8月份")
    elif a == 3 :
        print("该季度有9,10,11月份")
    elif a == 4:
        print("该季度有12,1,2月份")