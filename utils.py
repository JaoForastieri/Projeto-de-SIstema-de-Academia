import os #import de biblioteca para limpar os terminais

#função para limpar o terminal e deixar organizado.
def limpar():
    os.system('cls')

#função para inserir título e deixar bonito.
def titulo(texto):
    x = ' '
    print(f'\n{"-=-" * 15}\n {x*11} {texto.upper()}   \n{"-=-" * 15}')

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

