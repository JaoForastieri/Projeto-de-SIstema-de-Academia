
#listas para armazenar os valores.

lista_alunos = [] #armazenamento dos alunos.
lista_fila = [] #armazenamento da fila presencial de atendimento.
pessoas_pago =[] #armazenamento dos clientes que efetuaram o pagamento.
pessoas_pendente = [] #armazenamento dos clientes que ainda não efetuaram o pagamento.
lista_checkins = [] #armazenamento da lista dos clientes que fizeram check-in. 
fila = [] #armazenamento da 

PLANOS_DISPONIVEIS = {   
    'Básico': 69.90,
    'Gold': 129.90,
    'Black': 219.90
}.lower()

STATUS_PAGAMENTO = ('Pendente', 'Pago').lower()
DIAS_DA_SEMANA = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo').lower()
MODALIDADES = {
    'Musculação' : 1,   
    'Natação' : 2,
    'Judô' : 3,
    'Boxe' : 4,
    'Yoga' :5
}.lower()


