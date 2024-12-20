file=open('code.txt.txt','r')
print(file.read())
file.close()

file=open('code.txt.txt','r')
print(file.read(5))
file.close()

file=open('code.txt.txt','a')
file.write("Hi my name Adhrit Narayanan Kc and I am 14 years old")
file.close()