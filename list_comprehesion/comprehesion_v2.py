dobros_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobros_pares)

# versao normal:

dobros_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_pares.append(i*2)
        dobros_pares.append(i*2)
print(dobros_pares)