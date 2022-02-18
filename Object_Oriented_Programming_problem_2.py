from self import Employee


class Calculator:
    def __init__(self, number):
        self.number = number

    def square_of_num(self):
        print(f"The value of {self.number} square is {self.number ** 2}")

    def squareRoot_of_num(self):
        print(
            f"The value of {self.number} square root is {self.number ** 0.5}")

    def cube_of_num(self):
        print(f"The value of {self.number} cube is {self.number ** 3}")

    @staticmethod
    def time():
        print("The time of the sosd sj")

    @staticmethod
    def greet():
        print("Hello")


a = Calculator(2)
a.greet()
a.time()
a.square_of_num()
a.squareRoot_of_num()
a.cube_of_num()




        