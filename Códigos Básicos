import random

#Função para criar um Menu de escolhas
def menu():
    sair = ''
    while sair != 'N':
        opcao = int(input('Insira o número de qual rotina testar:\n1- Adivinhe um número aleatório entre 1 e 10\n2- Escolha um número entre 1 e n para que o computador adivinhe\n3- Jogue Pedra/Papel/Tesoura\n '))
        if opcao == 1:
            chute_numerico()
        if opcao == 2:
            chute_computador()
        if opcao == 3:
            pedra_papel_tesoura()
        sair = input('\nDeseja testar outra rotina?(S/N) ').upper()

#Função para adivinhar um número aleatório de 1 a 10
def chute_numerico():
    numero = random.randint(1,10)
    while True:
        chute = int(input('\nInsira um número de 1 a 10: '))
        if chute == numero:
            break
        if chute < numero:
            print('Tente um número maior')
        if chute > numero:
            print('Tente um número menor')
    print(f'Acerto! O número era {numero}\n')

#Função para o computador adivinhar um número
def chute_computador():
    x = int(input('\nInsira o número máximo que pode ser escolhido: '))
    minimo = 1
    maximo = x
    feedback = ''
    while feedback != 'CERTO' and minimo != maximo:
        chute_pc = random.randint(minimo, maximo)
        feedback = input(f'O numero {chute_pc} é Maior / Menor / Certo em relação ao escolhido? ').upper()
        if feedback == "MAIOR":
            maximo = chute_pc -1
        elif feedback == "MENOR":
            minimo = chute_pc + 1
    print(f"O numero escolhido foi {chute_pc}\n")

#Função para jogo aleatório de Pedra/Papel/Tesoura
def pedra_papel_tesoura():
    mais = ''
    score = 0
    score_pc = 0
    while mais != 'N':
        escolha = input("\nEscolha entre Pedra / Papel / Tesoura ").upper()
        if escolha not in ["PEDRA","PAPEL","TESOURA"]:
            escolha = input("\nEscolha entre Pedra / Papel / Tesoura ").upper()
        escolha_pc = random.choice(["PEDRA","PAPEL","TESOURA"])
        if escolha == escolha_pc:
            mais = input("\nEmpate!! Mais uma?(S/N) ").upper()
        elif ((escolha == "PEDRA" and escolha_pc == "TESOURA") or (escolha == "TESOURA" and escolha_pc == "PAPEL") or (escolha == "PAPEL" and escolha_pc == "PEDRA")):
            score += 1
            mais = input(f'\nVoce ganhou!!\nVoce escolheu {escolha} e o PC {escolha_pc}.\nPlayer: {score} x PC {score_pc}. Mais uma?(S/N) ').upper()
        else:
            score_pc += 1
            mais = input(f'\nPC ganhou!!\nVoce escolheu {escolha} e o PC {escolha_pc}. \nPlayer: {score} x PC {score_pc}. Mais uma?(S/N) ').upper()
    print(f'\n\nPlacar final -- Jogador: {score} e PC: {score_pc}\n')

menu() 
