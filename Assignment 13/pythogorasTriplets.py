n=int(input())
count =0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i<j<k:
                square = i**2 + j**2 
                if square == (k**2):
                    count += 1
print(count)