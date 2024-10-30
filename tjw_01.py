num = int(input("请输入一个三位整数："))
ge = num %10
shi = num / 10 % 10
bai = num / 100 % 10
print("这个三位数的逆序是：%d%d%d" % (ge,shi,bai) )