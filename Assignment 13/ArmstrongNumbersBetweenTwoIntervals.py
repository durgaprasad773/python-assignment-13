m=int(input())
n=int(input())
row=""
for i in range(m,n+1):
    num = str(i)
    sum_of = 0
    length = len(num)
    for j in num:
        sum_of = sum_of + (int(j) ** length)
    if sum_of == i:
        row = row + str(sum_of) +" "
        
if len(row) > 0:
    print(row)
else:
    print(-1)