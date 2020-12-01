from sys import exit

numbers = []
with open('input.txt', 'r') as f:
    for row in f:
        numbers.append(int(row))

for key_i, i in enumerate(numbers):
    for key_j, j in enumerate(numbers):
        if key_i == key_j:
            continue
        if i+j == 2020:
            print(i*j)
            exit(0)