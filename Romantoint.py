roman_numeral="XIX"
roman_numeral=roman_numeral.replace("IV","IIII")
roman_numeral=roman_numeral.replace("IX","VIIII")
roman_numeral=roman_numeral.replace("XL","XXXX")
roman_numeral=roman_numeral.replace("XC","LXXXX")
roman_numeral=roman_numeral.replace("CD","CCCC")
roman_numeral=roman_numeral.replace("CM","DCCCC")
roman_values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
seperated=[]
total=[]
for letter in roman_numeral:
    seperated.append(letter)    
for i in range(len(seperated)):
    if seperated[i] in roman_values:
        total.append(roman_values[seperated[i]])
print(sum(total))