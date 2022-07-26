def fibonacci(limite=10):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end='')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(f', {ultimo}', end='')


fibonacci(100)