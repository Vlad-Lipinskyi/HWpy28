print("Завдання 1")

def primeGenerator():
    currentNumber = 2
    while True:
        isPrime = True
        for divisor in range(2, int(currentNumber ** 0.5) + 1):
            if currentNumber % divisor == 0:
                isPrime = False
                break
        if isPrime:
            yield currentNumber
        currentNumber += 1

gen = primeGenerator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print("")
print("Завдання 2")
