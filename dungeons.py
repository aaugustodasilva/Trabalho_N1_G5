import random

lista_casas = {
    1: {
        'Direita': 2,
        'Esquerda': 3
    },
    2: {
        'Direita': 3,
        'Esquerda': 4
    },
    3: {
        'Direita': 4,
        'Esquerda': 5  
    },
    4: {
        'Direita': 5,
        'Esquerda': 6,
    },
    5: {
        'Direita': 6,
        'Esquerda': 7,
    },
    6: {
        'Esquerda': 8
    },
    7: {
        'Direita': 8,
        'Esquerda': 9
    },
    8: {
        'Direita': 9,
        'Esquerda': random.choice([1, 2, 3, 4, 5])
    }
}

interação_atual = 0
casa = 1
print("Olá! Seja bem-vindo ao Dungeons - Grupo 5.\n")
Guilda = (input("Digite o nome da sua Guilda:\n"))
print("A guilda " + Guilda + " começa na sala 1 e precisa chegar na sala 9 podendo escolher somente dois caminhos.\n")
print("Direita ou Esquerda\n")

while (casa != 9):
    print("Você está na casa " + str(casa) +"!")
    print("Suas opções: " + str(lista_casas.get(casa))+" ")
    casa = int(input(print("Selecione uma opção: ")))
    interação_atual += 1
    print("Interações: " +str(interação_atual)+"")
    if(interação_atual <=7 and casa == 9):
        print("Você Venceu!")
    elif(casa == 8):
        print("Se você escolher esquerda, cairá no portal e terá que voltar para a casa selecionada!")
print("\nFim")
