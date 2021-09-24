import random

lista_casas = {
    1: {
        'direita': 2,
        'esquerda': 3
    },
    2: {
        'direita': 3,
        'esquerda': 4
    },
    3: {
        'direita': 4,
        'esquerda': 5  
    },
    4: {
        'direita': 5,
        'esquerda': 6,
    },
    5: {
        'direita': 6,
        'esquerda': 7,
    },
    6: {
        'esquerda': 8
    },
    7: {
        'direita': 8,
        'esquerda': 9
    },
    8: {
        'direita': 9,
        'esquerda': random.choice([1, 2, 3, 4, 5])
    }
}

interação_atual = 0
casa = "1"
print("Olá! Seja bem-vindo ao Dungeons - Grupo 5.\n")
Guilda = (input("Digite o nome da sua Guilda:\n"))
print("A guilda " + Guilda + " começa na sala 1 e precisa chegar na sala 9 podendo escolher somente dois caminhos.\n")
print("direita ou esquerda\n")

print("Você está na casa " + casa +"!\n")

while (casa != 9):
    interaçao_atual = interação_atual + 1
    casa = int(input(print("Selecione uma opção: ")))
    print(lista_casas.get(casa))
    print(interação_atual)
print("\nFim")

#print(lista_casas.keys(), lista_casas.values())

#print("A casa é" + casa +"!")
