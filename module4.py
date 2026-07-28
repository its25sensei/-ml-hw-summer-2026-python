n = int(input())

numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)
x = int(input())

if x in numbers:
    print(numbers.index(x) + 1)
else:
    print(-1)