temp = float(input("请输入温度值："))
unit = input("请输入温度单位：")
unit2 = input("请输入需要转换后的单位:")
if unit == unit2 :
    print("转换后温度为:%d%s" % (temp,unit2))
elif unit =='c' :
    if unit2 == 'f' :
        temp = temp*1.8+32
    elif unit == 'k' :
        temp = temp + 237.15
elif unit =='f' :
    if unit2 == 'c' :
        temp = (temp-32)/1.8
    elif unit2 =='k' :
        temp = (temp-32)/1.8 + 237.15
elif unit == 'k' :
        if unit2 == 'c' :
            temp = temp - 237.15
        elif unit == 'f' :
            temp = temp * 9 / 5 -459.67
print("转换后的温度为：%d%c" %(temp,unit2))

