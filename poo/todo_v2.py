from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possivel indexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendente(s))'

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
    casa = Projeto('Tarefas de casa')
    casa.add('Lavar as roupas')
    casa.add('Passar roupa')
    print(casa)
    casa.procurar('Lavar as roupas').concluir()
    #[tarefa.concluir() for tarefa in casa.tarefas if tarefa == 'Lavar as roupas']
    for tarefas in casa.tarefas:
        print(f'- {tarefas}')
    print(casa)

main()
