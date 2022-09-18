list1=[5,4,3]
list2=[4,2,4]
num1=str(list1[len(list1)-1])
num2=str(list2[len(list2)-1])
i=len(list1)-2
while i>=0:
    num1=num1+str(list1[i])
    num2=num2+str(list2[i])
    i=i-1
num1=int(num1)
num2=int(num2)
print(num1+num2)