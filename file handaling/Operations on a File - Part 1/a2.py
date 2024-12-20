file=open('code.txt.txt','r')
print(file.read())
file.close()

file=open('code.txt.txt','w')
file.write("My name is Adhrit")
file.close()

file=open('code.txt.txt','a')
file.write(" and I learn Python in Codingal")
file.close()

file=open('python.txt','r')
print("Multiple lines-")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('python.txt','r')
print("Single line-")
print(file.readline())
file.close()

file=open('python.txt','r')
print("looping through the lines-")
for line in file:
    print(line)
file.close()