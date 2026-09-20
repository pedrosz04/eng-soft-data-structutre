def interface():
    print("   0,   1,   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))
 
 
def verificarVitoria(rodada):
    # Linhas
    for i in range(3):
        if tabuleiro[i][0] == rodada and tabuleiro[i][1] == rodada and tabuleiro[i][2] == rodada:
            return True
 
    # Colunas
    for j in range(3):
        if tabuleiro[0][j] == rodada and tabuleiro[1][j] == rodada and tabuleiro[2][j] == rodada:
            return True
 
    # Diagonais
    if tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada:
        return True
 
    if tabuleiro[0][2] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][0] == rodada:
        return True
 
    return False
 
 
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
 
parar = False
rodada = "X"
jogadas = 0
 
while not parar:
    interface()
 
    try:
        linha = int(input("Digite a linha escolhida (0-2): "))
        coluna = int(input("Digite a coluna escolhida (0-2): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.\n")
        continue
 
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Posição inválida! Digite valores entre 0 e 2.\n")
        continue
 
    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já foi ocupada!\n")
        continue
 
    tabuleiro[linha][coluna] = rodada
    jogadas += 1
 
    if verificarVitoria(rodada):
        interface()
        print("O {} Venceu!".format(rodada))
        parar = True
    elif jogadas == 9:
        interface()
        print("Empate!")
        parar = True
    else:
        rodada = "O" if rodada == "X" else "X"
 
print("Programa Encerrado.")
