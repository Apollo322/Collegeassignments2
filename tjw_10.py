sum = 0
for i in range(1, 101):
    if i % 3 != 0:
        continue
    else:
        sum += i
print("结果是%d"% (sum))