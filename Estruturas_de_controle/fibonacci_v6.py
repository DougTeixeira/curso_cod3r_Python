def fibonacci(quantidade=10):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if quantidade == len(resultado):
            break
    return resultado


for fib in fibonacci(10):
    print(fib, end=' ')