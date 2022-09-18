nums=[3,3]
x=0
j=0
target=6
while x<len(nums):
    if x==j:
        pass
    elif nums[x]+nums[j]==target:
        print(x,j)
        break
    j=j+1
    if j/len(nums)==1:
        j=0
        x=x+1

