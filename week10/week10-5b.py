a = int(input('請輸入一整數'))

ans = 0
for i in range(1, a+1):
  print('現在測試', a, i, '相除的結果', a%i )
  if a%i == 0:
    ans += 1

print(ans)
# 小心,在剪貼程式時, TAB 及空格, 在不同環境下不一樣, 要Ctrl-A全選,便可發現錯誤
