import random
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
for i in range(100):
 num=random.randrange(1,7)
 print(num)

 if num==1:
  n1+=1
 elif num==2:
  n2+=1
 elif num==3:
  n3+=1
 elif num==4:
  n4+=1
 elif num==5:
  n5+=1
 else:
  n6+=1
 
print(f"Num 1: {n1}")
print(f"Num 2: {n2}")
print(f"Num 3: {n3}")
print(f"Num 4: {n4}")
print(f"Num 5: {n5}")
print(f"Num 6: {n6}")