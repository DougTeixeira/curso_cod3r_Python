bloco_atrs = ('bloco_acesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_arts(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items()
                    if k in suportados)


def tag_bloco(conteudo, *args, classe='sucess', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    return f'<{tag} {get_arts(novos_atrs, bloco_atrs)}class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    #<ul><li>item</li><li>item2</li> etc
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul> {get_arts(novos_atrs, ul_atrs)} {lista}</ul>'


if __name__=='__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e bloco', classe='info', inline=True))
    print(tag_bloco('info', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='Info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='Info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='Info',
                    bloco_acesskey='m', bloco_id='conteudo', ul_id='lista'))