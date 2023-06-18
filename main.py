
class Maths:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b


class Physics:
    @staticmethod
    def velocity(distance, time):
        return distance / time

    @staticmethod
    def acceleration(velocity, time):
        return velocity / time

    @staticmethod
    def force(mass, acceleration):
        return mass * acceleration

    @staticmethod
    def energy(mass, velocity):
        return 0.5 * mass * (velocity ** 2)

    @staticmethod
    def power(work, time):
        return work / time


def main():
    while True:
        subject = input("Which subject do you want to calculate: 'maths' or 'physics'? ").lower()

        if subject == "maths":
            operation = input("Choose an operation: 'addition', 'subtraction', 'multiplication', 'division', 'power': ")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == "addition":
                result = Maths.addition(num1, num2)
            elif operation == "subtraction":
                result = Maths.subtraction(num1, num2)
            elif operation == "multiplication":
                result = Maths.multiplication(num1, num2)
            elif operation == "division":
                result = Maths.division(num1, num2)
            elif operation == "power":
                result = Maths.power(num1, num2)
            else:
                print("Invalid operation!")
                continue

        elif subject == "physics":
            operation = input("Choose an operation: 'velocity', 'acceleration', 'force', 'energy', 'power': ")
            if operation == "velocity":
                distance = float(input("Enter the distance: "))
                time = float(input("Enter the time: "))
                result = Physics.velocity(distance, time)
            elif operation == "acceleration":
                velocity = float(input("Enter the velocity: "))
                time = float(input("Enter the time: "))
                result = Physics.acceleration(velocity, time)
            elif operation == "force":
                mass = float(input("Enter the mass: "))
                acceleration = float(input("Enter the acceleration: "))
                result = Physics.force(mass, acceleration)
            elif operation == "energy":
                mass = float(input("Enter the mass: "))
                velocity = float(input("Enter the velocity: "))
                result = Physics.energy(mass, velocity)
            elif operation == "power":
                work = float(input("Enter the work: "))
                time = float(input("Enter the time: "))
                result = Physics.power(work, time)
            else:
                print("Invalid operation!")
                continue

        else:
            print("Invalid subject!")
            continue

        print(f"The result is: {result}\n")

        repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
        if repeat != "yes":
            break


if __name__ == "__main__":
    main()


