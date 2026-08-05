from module5_mod import Numberlist

N = int(input("Enter positive N: "))
while N <= 0:
    N = int(input("N must be positive. Enter positive N: "))

numbers = Numberlist()
for i in range(N):
    numbers.insert(int(input(f"Enter number {i + 1}: ")))

x = int(input("Enter x: "))
print(numbers.search(x))