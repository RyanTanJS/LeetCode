number=400
romanarray=[]
while number!=0:
    if number>=1000:
        while number>=1000:
            romanarray.append("M")
            number=number-1000
    if number>=900:
        while number>=900:
            romanarray.append("CM")
            number=number-900
    if number>=500:
        while number>=500:
            romanarray.append("D")
            number=number-500
    if number>=400:
        while number>=400:
            romanarray.append("CD")
            number=number-400
    if number>=100:
        while number>=100:
            romanarray.append("C")
            number=number-100
    if number>=90:
        while number>=90:
            romanarray.append("XC")
            number=number-90
    if number>=50:
        while number>=50:
            romanarray.append("L")
            number=number-50
    if number>=40:
        while number>=40:
            romanarray.append("XL")
            number=number-40
    if number>=10:
        while number>=10:
            romanarray.append("X")
            number=number-10
    if number>=9:
        while number>=9:
            romanarray.append("IX")
            number=number-9
    if number>=5:
        while number>=5:
            romanarray.append("V")
            number=number-5
    if number>=4:
        while number>=4:
            romanarray.append("IV")
            number=number-4
    if number>=1:
        while number>=1:
            romanarray.append("I")
            number=number-1
print("".join(romanarray))