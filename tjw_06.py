money1 = int(input("请输入收款金额:"))
money2 = int(input("请输入付款金额："))
if money1  >= 100 :
    money1 = money1 / 10 * 9
if money2 < money1 :
    print("付款还差%d元"%(money1 - money2))
elif money2 > money1 :
    print("应找回%d元"%(money2-money1))
else:
    print("付款等于收款")