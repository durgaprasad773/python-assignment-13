n=int(input())
k=int(input())
count = n-1
for i in range(1,k+1):
    count = count + i
#print(count)

for i in range(1,k+1):
    row=""
    for j in range(i): 
        row = row + str(count) +" "
        count = count - 1
    print(row)