empty_dict={}
dict1={1:"School",2:"Coding",3:"Python",4:"Programming",5:"Computer"}

dict2={"Event":"Dance","Festival":"Bihu","Language":"Assamese","Tesla":"Elon Musk"}

print("The value of the key 1 is-", dict1[1])

print("The value after get operation is", dict1.get(6,"Not found"))

dict1[7]="Codingal"
print("The dictionary after adding a new key and value is-", dict1)

dict1[4]="Computer programming"
print("The dictionary after i change the value is-", dict1)

dict1.pop(4)
print("The dictionary after removing the value is-", dict1)

dict1.clear()
print("The dictionary after the clear operation is-",dict1)