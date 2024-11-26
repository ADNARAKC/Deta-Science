class Employee:
    def __init__(self):
        print("Employee record created")
    
    def __del__(self):
        print("Employee record deleted")

def creatObj():
    print("Making an object")
    obj1=Employee()
    

creatObj()