try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('nome: {}, idade: {}'.format(registro.strip().split(',')))
finally:
    print('finally')
    arquivo.closed

if arquivo.closed:
    print('O arquivo foi fechado')