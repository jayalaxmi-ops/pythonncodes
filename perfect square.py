num=int(input())
is_square=False
for i in range(1,num+1):
    if i*i==num:
        is_square=True
        break
if is_square:
    print(num,"is a perfect square")
else:
    print(num,"is not a perfect square")
