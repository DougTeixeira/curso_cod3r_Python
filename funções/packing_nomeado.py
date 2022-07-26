# **kwargs recebem parametros nomeados e criam um dicionario

def resultado_podium(**podium):
    for k, v in podium.items():
        print(f'{k} -> {v}')


resultado_podium(primeiro='L. Hamilton',
                 segundo='M. Verstappen', 
                 terceiro='S. Vettel')