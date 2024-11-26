s_1={1,2,3,4,5,6,7,8,9,10}
s_2={3,6,8,9,1,12,34,90,10}

print(f"Set 1 is {s_1}")
print(f"Set 2 is {s_2}")

print(f"The intersection of is {s_1.intersection(s_2)}")
print(f"The union is {s_1.union(s_2)}")
print(f"The difference between set1 and set2 is {s_1.difference(s_2)}")
print(f"The difference between set2 and set1 is {s_2.difference(s_1)}")

print(f"The Symmetric difference between set2 and set1 is {s_2.symmetric_difference(s_1)}")

s_1.add("Adhrit")
print(f"Set 1 after adding 'Adhrit' is {s_1}")

s_1.remove("Adhrit")
print(f"set 1  after removing 'Adhrit' is {s_1}")