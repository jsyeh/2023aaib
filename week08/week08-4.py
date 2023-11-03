# 接下來是排序的部分, 要示範Bubble泡泡排序時
# 先照著 https://www.youtube.com/watch?v=lyZQPjUT5B4
# 做一輪試試
a = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
N = len(a)
print(a) # 排之前, 印一下
for i in range(1,N):
  if a[i] < a[i-1]: # 比大小, 不對的話
    a[i], a[i-1] = a[i-1], a[i] # 就左右交換
print(a) # 排一輪之後, 再印一下