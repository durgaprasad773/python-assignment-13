n=int(input())

for i in range(n):
    row=""
    space=" " * i
    for j in range(1,n+1-i):
        row = row + str(j)+" "
    print(space + row)