# Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))