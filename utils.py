import os #import de biblioteca para limpar os terminais
from tarefas import id_pessoa

#função para limpar o terminal e deixar organizado.
def limpar():
    os.system('cls')

#função para inserir título e deixar bonito.
def titulo(str):
    x = ' '
    print(f'\n{"-=-" * 15}\n {x*2} {str.upper()}   \n{"-=-" * 15}')

#função para preparar a tela de entrada que será usada em main.py
def main():
    limpar()
    input("""
          
    ██████╗ ███████╗███╗   ███╗      ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗ 
    ██╔══██╗██╔════╝████╗ ████║      ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗
    ██████╔╝█████╗  ██╔████╔██║█████╗██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║
    ██╔══██╗██╔══╝  ██║╚██╔╝██║╚════╝╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║
    ██████╔╝███████╗██║ ╚═╝ ██║       ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝
    ╚═════╝ ╚══════╝╚═╝     ╚═╝        ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
                    Aperte qualquer tecla para continuar.
    
    """)
    limpar()


def menu_modalidade():
    
 titulo('-=-=-=- Menu De Modalidades -=-=-=-')
 while True
  try:
    var = input("1. Musculação\n2. Natação\n3. Judô\n4. boxe\n5. Yoga\n\n Escolha sua modalidade:")
  except:
    print('Entrada Invalida!')
      

def concluir_sessao():
    
    planos = {
        Básico = 1,
        Gold = 3,
        Black = 5
    }

