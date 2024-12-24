with open ('python.txt','w') as file:
    file.write("Hi my name is Adhrit Narayanan K.C and I read in class 9.")
file.close()

with open('python.txt','r') as file:
    data=file.readlines()
    for line in data:
        w=line.split()
        print(w)
file.close