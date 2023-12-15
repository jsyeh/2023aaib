# SOIT107_BASE_010
a = int(input())

# 31 28 31 30 31 30 31  31 30 31 30 31
#    2     4     6         9     11
if a==2: ans = 28
elif a==4 or a==6 or a==9 or a==11: ans = 30
else ans = 31
print(ans, end='' )