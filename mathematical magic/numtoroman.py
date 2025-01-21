def convert(num):
    roman={"I":1,"V":5, "X":10, "L":50, "C":100, "M":1000}
    result=0
    for i in range(0,len(num)-1):
        if (roman[num[i]]<roman[num[i+1]]):
            result-=roman[num[i]]
        else:
            result += roman[num[i]]
    return result+roman[num[-1]]
num=(input("Enter the number: "))
print("The roman neumerical of the number is:",convert(num))        