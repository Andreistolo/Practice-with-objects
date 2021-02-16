class Calculator:
    
    number1 = 0.0
    number2 = 0.0

    def add(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2 

    def mul(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 / self.number2  

calc = Calculator()

calc.number1 = 3
calc.number2 = 9
print("Addition of 3 and 9 is: ", calc.add())
print("Subtraction of 3 and 9 is: ", calc.sub())
print("Multiplication of 3 and 9 is: ", calc.mul())
print("Division of 3 and 9 is: ", calc.div())








    
