from sys import exit

numbers = []
with open('input.txt', 'r') as f:
    for row in f:
        numbers.append(int(row))

for key_i, i in enumerate(numbers):
    for key_j, j in enumerate(numbers):
        for key_k, k in enumerate(numbers):
            if key_i == key_j or key_i == key_k or key_j == key_k:
                continue
            if i+j+k == 2020:
                print(i*j*k)
                exit(0)