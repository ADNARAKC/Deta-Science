file=open('code.txt.txt','r')
file1=open('empty.txt','w')
count=file.readlines()
type(count)
for i in range (1,len(count)+1):
    if (i%2!=0):
        file1.write(count[i-1])
    else:
        pass
file1.close()

file1=open('empty.txt','r')
count1=file1.read()
print(count1)
file1.close()
file.close()