class Computer:
    def __init__(self):
        self.__max_price=99000
    def Sell(self):
        print(f"You have to pay rs {self.__max_price}")
    def max_price(self,price):
        self.__max_price=price
compt1=Computer()
compt1.Sell()
compt1.__max_price=100000
compt1.Sell()
compt1.max_price(100000)
compt1.Sell()