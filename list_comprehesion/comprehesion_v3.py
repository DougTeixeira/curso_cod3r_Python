import sys

# generator gasta menos memoria

generator = (i * 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # primeiro valor 0
print(next(generator)) # segundo valor 4 e etc

# teste de quantidade de memoria gasta
sys.getsizeof(generator)