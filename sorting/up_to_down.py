N = int(input())

array = []

for i in range(N):
    array.append(int(input()))
    
array.sort(reverse=True)

for i in range(len(array)):
    if i==len(array)-1:
        print(array[i])
    else:
        print(array[i],end=' ')