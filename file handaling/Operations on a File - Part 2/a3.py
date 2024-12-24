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