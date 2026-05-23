import os #import de biblioteca para limpar os terminais

#função para limpar o terminal e deixar organizado.
def limpar():
   os.system('cls' if os.name == 'nt' else 'clear')

#função para inserir título e deixar bonito.
def titulo(texto):
    print(f"\n{'—' * 15} {texto.upper()} {'—' * 15}\n")

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
 while True:
  try:
    var = input("1. Musculação\n2. Natação\n3. Judô\n4. boxe\n5. Yoga\n\n Escolha sua modalidade:")
    if var in ['1', '2', '3', '4', '5']:
            return var
  except:
    print('Entrada Invalida!')
      

def concluir_sessao():

    planos = {
        'basico': 1,
        'gold': 3,
        'black': 5
    }

    return planos
