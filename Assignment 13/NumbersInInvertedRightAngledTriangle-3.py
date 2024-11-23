s=int(input())
n=int(input())
count = s-1
for i in range(1,n+1):
    count = count + i
#print(count)

for i in range(n):
    row=""
    for j in range(1,n+1-i):
        row = row + str(count) +" "
        count = count - 1
    print(row)