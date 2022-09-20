array=[1,1,1,1,1,2,4]
x=0
for a in range(len(array)):
    if array.count(array[x])>1:
        array.pop(x)
    else:
        x=x+1
print(array)
