def fibonacci(quantidade=10, sequencia = (0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


for fib in fibonacci(10):
    print(fib)