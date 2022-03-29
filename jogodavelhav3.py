import os
from random import randint

# Variáveis globais
matriz = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# Funções
def printBoard():
    print("  =============  \n  JOGO DA VELHA  \n  =============")
    print("    0   1   2 ")
    print(f"0:  {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} ")
    print("   -----------")
    print(f"1:  {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} ")
    print("   -----------")
    print(f"2:  {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} ")

def vez_jogador():
    print("\n")
    print("Indique a linha e a coluna onde você quer colocar o X")
    l = int(input("Linha: "))
    c = int(input("Coluna: "))
    erro1 = l < 0 or l > 2
    erro2 = c < 0 or c > 2
    while erro1 or erro2:        
        os.system('cls')
        printBoard()
        print("\n")
        print("Índice inválido!")
        print("Indique a linha e a coluna onde você quer colocar o X")
        l = int(input("Linha: "))
        c = int(input("Coluna: "))
        erro1 = l < 0 or l > 2
        erro2 = c < 0 or c > 2    
        
    while matriz[l][c] != " ":
        os.system('cls')
        printBoard()
        print("\n")
        print("Indique a linha e a coluna onde você quer colocar o X")
        l = int(input("Linha: "))
        c = int(input("Coluna: "))
    matriz[l][c] = 'X'

def vez_robo():
    lr = randint(0, 2)
    cr = randint(0, 2)
    while matriz[lr][cr] != " ":
        lr = randint(0, 2)
        cr = randint(0, 2)
    matriz[lr][cr] = 'O'


# Programa
Xpts = 0
Opts = 0
resposta = 'S'
while resposta in 'Ss':
    jogada = 1
    while jogada <= 6:
        if jogada <= 4:
            os.system('cls')
            printBoard()
            vez_jogador()    
            vez_robo()
        elif jogada == 5:
            os.system('cls')
            printBoard()
            vez_jogador()
        else:
            os.system('cls')
            printBoard()

        # Casos Jogador X         
        XDiagonal1 = matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X'
        XDiagonal2 = matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X'
        XLinha0 = matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X'
        XLinha1 = matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X'
        XLinha2 = matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X'
        XColuna0 = matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X'
        XColuna1 = matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X'
        XColuna2 = matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X'    

        if XDiagonal1 or XDiagonal2 or XLinha0 or XLinha1 or XLinha2 or XColuna0 or XColuna1 or XColuna2: 
            os.system('cls')
            printBoard()
            print("\nVitória! Parabéns Jogador X!")
            break
        

        # Casos Robo 
        ODiagonal1 = matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O'
        ODiagonal2 = matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O'
        OLinha0 = matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O'
        OLinha1 = matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O'
        OLinha2 = matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O'
        OColuna0 = matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O'
        OColuna1 = matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O'
        OColuna2 = matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' 

        if ODiagonal1 or ODiagonal2 or OLinha0 or OLinha1 or OLinha2 or OColuna0 or OColuna1 or OColuna2: 
            os.system('cls')
            printBoard()
            print("\nDerrota!")
            break 

        jogada += 1

        
    XDiagonal1 = matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X'
    XDiagonal2 = matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X'
    XLinha0 = matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X'
    XLinha1 = matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X'
    XLinha2 = matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X'
    XColuna0 = matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X'
    XColuna1 = matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X'
    XColuna2 = matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X'  

    ODiagonal1 = matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O'
    ODiagonal2 = matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O'
    OLinha0 = matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O'
    OLinha1 = matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O'
    OLinha2 = matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O'
    OColuna0 = matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O'
    OColuna1 = matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O'
    OColuna2 = matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' 

    
    # Casos Jogador X     
    if XDiagonal1 or XDiagonal2 or XLinha0 or XLinha1 or XLinha2 or XColuna0 or XColuna1 or XColuna2: 
        os.system('cls')
        printBoard()
        print("\nVitória! Parabéns Jogador X!") 
        Xpts = Xpts + 1  
        

    # Casos Robo     
    elif ODiagonal1 or ODiagonal2 or OLinha0 or OLinha1 or OLinha2 or OColuna0 or OColuna1 or OColuna2: 
        os.system('cls')
        printBoard()
        print("\nDerrota!")
        Opts = Opts + 1

    # Caso empate
    else:
        print("\nDeu velha!")


    print(f"\nPontuação: \nX: {Xpts} pontos \nO: {Opts} pontos ")

    resposta = input("Quer jogar novamente? [S/N] ")

    while resposta not in 'SsNn':
        os.system('cls')
        printBoard()
        print("\n")
        print(f"\nPontuação: \nX: {Xpts} pontos \nO: {Opts} pontos ")
        print("Resposta Inválida!")       
        resposta = input("Quer jogar novamente? [S/N] ") 

   
    if resposta in 'Ss':
        matriz = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
    