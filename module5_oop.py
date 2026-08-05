class Numberlist:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, number):
        for i in range(len(self.numbers)):
            if self.numbers[i] == number:
                return i + 1
        return -1

N = int(input("Enter positive N: "))
while N <= 0:
    N = int(input("N must be positive. Enter positive N: "))

numbers = Numberlist()
for i in range(N):
    numbers.insert(int(input(f"Enter number {i + 1}: ")))

x = int(input("Enter x: "))
print(numbers.search(x))