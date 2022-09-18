num=1441
num=str(num)
array=[]
for letter in num:
    array.append(letter)
x=0
i=len(array)-1
while x<len(array):
    if array[x]==array[i]:
        pass
    else:
        print('number is not a palidrome number')
        break
    if x>=i:
        print("This is a palidrome number")
        break
    x=x+1
    i=i-1