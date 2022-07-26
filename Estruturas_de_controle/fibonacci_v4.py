def fibonacci(limite=10):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-1]+resultado[-2])
    return resultado


for fib in fibonacci(100):
    print(fib, end=' ')