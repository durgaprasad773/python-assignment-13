n=int(input())
for i in range(1,n+1):
    space=" " * (n-i)
    row=""
    for j in range(1,i+1):
        row = row + str(j)+" "
    print(space + row)
    
for i in range(1,n):
    space=" " * i
    row =""
    for j in range(1,n-i+1):
        row = row + str(j)+" "
    print(space + row )