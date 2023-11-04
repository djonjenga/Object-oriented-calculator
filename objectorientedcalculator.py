#JOSEPH NJENGA
#SCT211-0040/2022
class AdditionCalculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def get_result(self):
        return self.result


calculator = AdditionCalculator()

while True:
    print("Options:")
    print("Enter 'add' to perform addition")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        calculator.add(num1, num2)
        print("Result:", calculator.get_result())
    else:
        print("Invalid input. Please enter a valid operation.")
