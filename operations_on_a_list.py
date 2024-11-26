lst=["Apple","Mango","Banana","Cherry","Strawberry"]
print("The third item on my list is-",lst[2])
print("The length of my list is-",len(lst))
print("Slicing",lst[2:4])

lst.append("Mango")
print("The list after the append operation is", lst)

lst.remove("Mango")
print("The list after removing the value is", lst)

lst.reverse()
print("The list after reversing the value is",lst)

lst.sort()
print("The list sfter the short operation is", lst)

lst.pop()
print("The list after the popp operation is", lst)

lst.clear()
print("The list after the clear operation is", lst)