import random
i=0
total = 0
while i<10:
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)
  a=num1+num2
  i+=1
  result =int(input("请输入%d+%d的值:"%(num1,num2)))
  if result == a :
      print("答案正确，加2分")
      total+=2
  else:
      print("答案错误，扣5分")
      total-=5
print("最终得分为%d"%(total))