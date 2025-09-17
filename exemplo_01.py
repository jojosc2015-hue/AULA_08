# Funções

def mensagem(nome):
    print(f'Olá,{nome}!!!!!')


def somar(n1, n2):
    s = n1 + n2
    print(f'O resultado é {s}')

# mensagem('Renato')
# mensagem('Maria')
# mensagem('José')

n1 = float(input('Primeiro Número:'))
n2 = float(input('Segundo Número:'))
somar(n1, n2)