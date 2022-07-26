with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('nome: {}, idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo foi fechado')
