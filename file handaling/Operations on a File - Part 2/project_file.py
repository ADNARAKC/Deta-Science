with open ('python.txt','w') as file:
    file.write("Hi my name is Adhrit Narayanan K.C and I read in class 9.")
file.close()

with open('python.txt','r') as file:
    data=file.readlines()
    for line in data:
        w=line.split()
        print(w)
file.close
new_file=open('m_file.txt','x')
new_file.close()
import os
print("Checking if m_file exists or not.")
if os.path.exists('m_file.txt'):
    os.remove('m_file.txt')
else:
    print("The file does not exists.")

my_file=open('my_file.txt','w')
my_file.write("Hi my name is Adhrit Narayanan KC.")
my_file.close()

os.remove('Codingal.txt')
os.rmdir('Folder')
output_file=open('output_file.txt','w')
input_file=open('Repeated.txt','r')
lines_seen=set()
print("Eliminating duplicated lines.")
for line in input_file:
    if line not in lines_seen:
        output_file.write(line)

        lines_seen.add(line)
input_file.close()
output_file.close()
with open('file_1.txt') as fp:
    data1=fp.read()
with open('file_2.txt') as fp:
    data2=fp.read()

data1+="\n"
data1+=data2
print("Merging two files.")
with open("Merged_files.txt",'w') as fp:
    fp.write(data1)