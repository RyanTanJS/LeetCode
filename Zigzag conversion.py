list=[[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]]
word=["P","A","Y","P","A","L","I","S","H","I","R","I","N","G" ]
n=4
x=0
j=0
c=0
letters=len(word)
while letters!=0:
    for a in range(n):
        if letters==0:
            break
        list[x][j]=word[c]
        c=c+1
        x=x+1
        letters=letters-1

    x=x-1
    for b in range(n-2):
        if letters==0:
            break
        j=j+1
        x=x-1

        list[x][j]=word[c]
        c=c+1
        letters=letters-1
    x=0
    j=j+1

