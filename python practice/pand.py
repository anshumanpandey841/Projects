class calculatior:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def __init__(self):
        print("Calculator initialized")

c = calculatior()
print(c.add(10, 5))
print(c.subtract(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))

