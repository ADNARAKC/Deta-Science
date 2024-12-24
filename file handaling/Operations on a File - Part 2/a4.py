with open('file_1.txt') as fp:
    data1=fp.read()
with open('file_2.txt') as fp:
    data2=fp.read()

data1+="\n"
data1+=data2
print("Merging two files.")
with open("Merged_files.txt",'w') as fp:
    fp.write(data1)