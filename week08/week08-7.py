#  (A030) 百數反印 : 輸入100個正整數，反向印出此100個數。 
a = input().split()

for i in range(100):
	a[i] = int(a[i])


for i in range(100-1, -1, -1):
	print(a[i])