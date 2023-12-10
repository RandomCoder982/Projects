import math

class Calculator:
    
    def __init__(self, calculator):
        self.calculator = calculator

    def add(num1, num2):
        ans = num1 + num2
        print(ans)
    def subtract(num1, num2):
        ans = num1 - num2
        print( ans)
    def multiply(num1, num2):
        ans = num1 * num2
        print(ans)
    def divide(num1, num2):
        if num1 != 0 and num2 == 0:
            print("You can not divide by 0")
        else:
            ans = num1/num2
            print(ans)

  

