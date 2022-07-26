def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


todos_params('a', 'b', 'c')
todos_params(1, 2, 3, legal=True, valor=12.99) 
todos_params('Ana', False, [1,2,3], tamanho='M', fragil=False)
todos_params(primeiro='joao', segundo='Maria')
todos_params('Maria', primeiro='joao')