from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (concluido)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')

    # for i in casa:
    #    if i.descricao == 'Lavar prato':
    #        i.concluir()
    #    print(f'- {i}')


main()
