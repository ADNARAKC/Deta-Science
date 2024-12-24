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