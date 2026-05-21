from dados import alunos, status, status_pendente, pilha_concluida
from utils import titulo

def cadastra_nomes ():
    titulo('Seja bem-vindo!')

    nome = input('Digite o seu nome: ')
    tuplas 
    modalidade = input('Digite a sua modalidade: ')
    dias = input('Digite os dias da semana que virá: ').lower()
    objetivo = input('Digite o seu objetivo: ')
    print('''planos: 
    [1] Básico
    [2] Gold
    [3] Black''' )

    plano = int(input('Digite o número de seu plano: '))

    print(' - status: 1. pendente | 2. pago ')
    status = input('status de pagamento: ')

    # Lê os status de pagamento da tupla pelo indíce
    if opcao == '1':
        status = status[0] #pendente
    elif opcao == '2':
        status = status[1] #pago

    # Cria o dicionário representando os cadrastos do aluno
    
     direct_cadasto = {
        'id': len(alunos) + 1
        'nome': nome
        'modalidade': modalidade
        'dia da semana': dias
        'objetivo': objetivo
        'pagamento': status
        }

        #adicione á lista principal
        alunos.append(direct_cadastro)

        #adicionar à fila pendente 
        status_pendente.append(direct_cadastro)

        print('Aluno cadastradas com sucesso!!!')


def listar_alunos_modalidade:
    titulo('Alunos por modalidade')

    # Se não tiver um aluno
    if len(alunos) == 0:
        print('Nenhum aluno em aulas com modalidade.')
        return
    
    for modalidade in modalidades:
        




# O que aparecerá na lista dos alunos.
def listar_alunos():
    titulo('Seu cadastro')

    for i, alunos in enumerate(alunos, start=1):
        print(f"ID: {i}")
        print(f"nome: {alunos['nome']}")
        print(f"modalidade: {alunos['modalidade']}")
        print(f"dia da semana: {alunos['dia da semana']}")
        print(f"objetivo: {alunos['objetivo']}")
        print(f"Status: {alunos['status']}")
        print() #linha em branco entre tarefas
        print()  


def atualizar_status():
    print('\n --- Atualizar status ---')
    listar_alunos()

    #Guarda 1: lista vasia - nada a atualizar
    if len(aluno) == 0:
        return

    # Guarda 2: usuário pode digitar texto em vez de 
    try: 
        id_pessoa = int(input('Digite o ID do aluno:'))
    except ValueError:
        print('Digite um número válido')
        return

    for alunos in aluno: # Ver o ID do aluno
        if alunos ['id'] == id_pessoa:
            print('\nEscolha o novo status:')
            print('''[1] Pendente
            [2] Pago''')
            opcao = input('Digite a sua opção: ')


            if opcao == '1': # Se for pendente 
                alunos['pagamento'] = status[0]
                if alunos not in fila_pendente:
                    fila_pendente.append(alunos) # empilhar

            elif opcao == '2':  # se está pago ou saiu do pendente
                alunos['status'] = status[1]
                pilha_concluida.append(alunos) 
                if alunos in fila_pendente:
                    fila_pendente.remove(alunos) # sai da fila
            

            print('Status atualizado com sucesso!!!')
            return

    print('Aluno não encontrada')

def historico():
    titulo('Histórico de pessoas pendente no pagamento')

    if len(fila_pendente) == 0:
     print('Nenhuma tarefa concluída.')
     return

    for i, alunos in enumerate(reversed(fila_pendente), start = 1):
        print(f'ID: {alunos['id']}')
        print(f"nome: {alunos['nome']}")
        print(f"modalidade: {alunos['modalidade']}")
        print()
        print()