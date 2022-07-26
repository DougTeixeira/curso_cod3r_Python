def fibonacci(limite=10):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end='')
    while ultimo <= limite:
        proximo = penultimo + ultimo
        print(f', {proximo}', end='')
        penultimo = ultimo
        ultimo = proximo


fibonacci(100)