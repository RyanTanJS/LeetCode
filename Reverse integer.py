number=-123
string2=str(number)
array=[*string2]
reversednumber=[]
if array[0]=="-":
    reversednumber.append("-")
    for a in range(len(array)-1):
        reversednumber.append(array[len(array)-1-a])

else:
    for a in range(len(array)):
        reversednumber.append(array[len(array)-a-1])
print("".join(reversednumber))
