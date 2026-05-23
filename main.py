from tarefas import cadastra_nomes, listar_alunos, atualizar_status, listar_alunos_modalidade, recepcao, historico, concluir_sessao
from utils import limpar, titulo, main

main()

while True:
    print('-=-=-'*8)
    print('1. Cadastrar Alunos')
    print('2. Alunos Por Modalidade')
    print('3. Fila de Atendimento')
    print('4. Lista de Alunos')
    print('5. Atualizar Status Aluno')
    print('6. Histórico de Pendências')
    print('7. Concluir Sessão')
    print('8. Sair')
    
    
    opcao = int(input('Digite sua escolha:'))
    
    if opcao == 1:
        cadastra_nomes()
    elif opcao == 2:
        listar_alunos_modalidade()
    elif opcao == 3:
        recepcao()
    elif opcao == 4:
        listar_alunos()
    elif opcao == 5:
        atualizar_status()
    elif opcao == 6:
        historico()
    elif opcao == 7:
        concluir_sessao()
    elif opcao == 8:
        print('Saindo do programa...')
        break
    else:
        print('Opção Inválida. Tente Novamente')
        continue
