from dados import lista_alunos, lista_fila, pessoas_pago, lista_checkins, fila, planos_disponiveis, status_pagamento, dias_da_semana, modalidades, pessoas_pendente
from utils import titulo
from datetime import datetime
 
dia = datetime.now().day, datetime.now().month, datetime.now().year
 
sessoes_por_plano = {1: 4, 2: 12, 3: 20} #qnt de sessões 
nome_plano = {1: 'Básico', 2: 'Gold', 3: 'Black'}
 
def cadastra_nomes ():
    titulo('Seja bem-vindo!')
 
    nome = input('Digite o seu nome: ')

 
    print(f'Modalidades disponíveis:')
    for nome_mod, num_mod in modalidades.items():   # itera o dict de dados.py
        print(f'  [{num_mod}] {nome_mod}')
    
    modalidade = input('Digite o número da modalidade: ').lower()
    dias = input('Digite os dias da semana que virá: ').lower()
    objetivo = input('Digite o seu objetivo: ')
    print('''planos disponíveis: 
    [1] Básico
    [2] Gold
    [3] Black''' )
 
    planos_opcao = int(input('Digite o número de seu plano: '))
 
    print(' - status: 1. pendente | 2. pago ')
    status = input('status de pagamento: ')
 
    # Lê os status de pagamento da tupla pelo indíce
    if status == '1':
        status_final = status_pagamento[0] #pendente
 
    elif status == '2':
        status_final = status_pagamento[1] #pago
 
     # Cria o dicionário representando os cadrastos do aluno
    novo_aluno = {
        'id': len(lista_alunos) + 1,
        'nome': nome,
        'modalidade': modalidade,
        'dia da semana': dias,
        'objetivo': objetivo,
        'plano': nome_plano.get(planos_opcao, 'Básico'),
        'pagamento': status_final,
        'status': status_final,
        'sessoes': []
        }
 
        #adicione á lista principa
    lista_alunos.append(novo_aluno)
 
        #adicionar à fila pendente 
    if status_final == status_pagamento[0]:
        pessoas_pendente.append(novo_aluno)
 
    print('Aluno cadastradas com sucesso!!!')
 
 
def listar_alunos_modalidade():
    titulo('Alunos por modalidade')
 
    # Se não tiver um aluno
    if len(lista_alunos) == 0:
        print('Nenhum aluno com modalidade.')
        return
    
    for modalidade, num in modalidades.items(): #
        print(f'----- {modalidade} -----')
 
        aluno_encontrado = False
 
        for aluno in lista_alunos:
            if aluno['modalidade'] == str(num):
                print(f'''
                  'ID': {aluno['id']} 
                  'Nome': {aluno['nome']} 
                  'Modalidade': {aluno['modalidade']} 
                  'Pagamento': {aluno['pagamento']}''')
 
def recepcao():
        while True: 
            print('\n=== FILA DA RECEPÇÃO ===')
            print('1 - Adicionar pessoa')
            print('2 - Atender pessoa')
            print('3 - Ver fila')
            print('4 - Sair')
 
            opcao = input('Digite o número de sua escolha: ')
 
             # Adicionar pessoa
            if opcao == '1':
                nome = input('Nome da pessoa: ')
 
              # Adiciona no final da lista
                fila.append(nome)
 
                print(f'{nome} entrou na fila.')
        
            elif opcao == '2':
                if len(fila) == 0:
                    print('Fila vazia.')
 
                else:# Remove o primeiro da fila
                    atendido = fila.pop(0)
                    print(f'{atendido} foi atendido.')
 
              # Mostrar fila
            elif opcao == '3':
                if len(fila) == 0:
                    print('Fila vazia.')
 
                else:
                    print('\nFila atual:')
                    for pessoa in fila:
                        print(pessoa)
 
              # Sair
            elif opcao == '4':
                print('Sistema encerrado.')
                break
            else:
              print('Opção inválida.')
 
# O que aparecerá na lista dos alunos.
def listar_alunos():
    titulo('Seu cadastro')
 
    for i, alunos in enumerate(lista_alunos, start=1):
        print(f"ID: {alunos['id']}")
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
    if len(lista_alunos) == 0:
        return
 
    # Guarda 2: usuário pode digitar texto em vez de 
    try: 
        id_pessoa = int(input('Digite o ID do aluno:'))
    except ValueError:
        print('Digite um número válido')
        return
 
    for aluno in lista_alunos: # Ver o ID do aluno
        if aluno ['id'] == id_pessoa:
            print('\nEscolha o novo status:')
            print('''[1] Pendente
            [2] Pago''')
            opcao = input('Digite a sua opção: ')
 
 
            if opcao == '1': # Se for pendente 
                aluno['pagamento'] = status_pagamento[0]
                if aluno not in pessoas_pendente:
                    pessoas_pendente.append(aluno) # empilhar
 
            elif opcao == '2':  # se está pago ou saiu do pendente
                aluno['status'] = status_pagamento[1]
                aluno['pagamento'] = status_pagamento[1]
                pessoas_pago.append(aluno) 
                if aluno in pessoas_pendente:
                    pessoas_pendente.remove(aluno) # sai da fila
            
 
            print('Status atualizado com sucesso!!!')
            return
 
    print('Aluno não encontrada')
 
def historico():
    titulo('Histórico de pessoas pendente no pagamento')
 
    if len(pessoas_pendente) == 0:
     print('Nenhuma tarefa concluída.')
     return
 
    for i, alunos in enumerate(reversed(pessoas_pendente), start = 1):
        print(f"ID: {alunos['id']}")
        print(f"nome: {alunos['nome']}")
        print(f"modalidade: {alunos['modalidade']}")
        print()
        print()

def concluir_sessao():
    planos = {
        'Básico': 1,
        'Gold': 3,
        'Black': 5
    }
    try:
        id_pessoa = int(input('Digite o ID do aluno: '))
    except ValueError:
        print('Entrada inválida.\nDigite apenas números inteiros e reais.')
        return

    for aluno in lista_alunos:
        if aluno['id'] == id_pessoa:
            plano_aluno = aluno ['plano']
            limite = planos[plano_aluno]

            #contar quantas sessões o aluno fez
            sessoes_feitas = len(aluno['sessoes'])
            if sessoes_feitas >= limite:
                print(f'O aluno {aluno[nome]} já utilizou todas as {limite} sessões do seu plano {plano_aluno}')
                return
            
            final = (sessoes_feitas + 1) / limite
            #registrar a nova sessão na planilha
            data = input('Digite a data da sessão (dia/mes/ano): ')
            aluno['sessoes'].append(data)
            print(f'''Sessão registrada com sucesso!!!!
                  O aluno {aluno[nome]} utilizou {final} sessões.''')
            return
    

            

