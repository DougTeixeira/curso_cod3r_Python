def fibonacci(quantidade=10):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


for fib in fibonacci(10):
    print(fib, end=' ')