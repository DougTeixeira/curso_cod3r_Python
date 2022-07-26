def fibonacci(limite=10):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end='')
    while True:
        proximo = penultimo + ultimo
        if proximo <= limite:
            print(f', {proximo}', end='')
            penultimo = ultimo
            ultimo = proximo
        else:
            break


fibonacci()