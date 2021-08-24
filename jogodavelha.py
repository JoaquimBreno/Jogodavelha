from tabulate import tabulate
# from contaxalinhados import contaXAlinhados
import random

def validaEntradaCorreta(letra, numero):
    """
    Confere se as coordenadas recebidas estão dentro das opções válidas
    Parâmetros: letra, numero
    Retorno: True(Opção válida)/False(Opção inválida)
    """
    if letra not in ["A", "B", "C"] or numero not in ["1", "2", "3"]:
        return False
    else:
        return True

def validaEntradaDisponivel(tabuleiro, letra, numero):
    """
    Confere se a coordenada recebida está disponível
    Parâmetros: tabuleiro, letra, numero
    Retorno: True(Disponivel)/False(Indisponivel)
    """
    if tabuleiro[letra][numero-1] != "":
        return False
    else:
        return True

def validaEntrada(tabuleiro, letraNumero):
    """
    Valida entrada do usuário para possíveis erros de digitação, cordenadas inválidas ou já utilizadas
    Parâmetros: tabuleiro, letraNumero (coordenadas da jogada)
    Retorno: letra e numero (coordenadas da jogada validadas)
    """
    # Valida digitações fora do esperado
    try:
        letra, numero = letraNumero.upper().split()
    except:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))
    # Se entrada correta e disponível retorna, caso contrário chama a função novamente
    if validaEntradaCorreta(letra, numero):
        if validaEntradaDisponivel(tabuleiro, letra, int(numero)):
            return letra, int(numero)
        else:
            return validaEntrada(tabuleiro, input(f"Coordenadas indisponíveis, digite uma livre: ")) 
    else:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))  

def jogada(tabuleiro):
    """
    Pede a jogada ao usuario e aplica ao tabuleiro
    Parâmetros: tabuleiro
    Retorno: tabuleiro
    """
    letra, numero = validaEntrada(tabuleiro, input(f"Vez do jogador: "))

    tabuleiro[letra][numero-1] = "O"

    return tabuleiro

def parabenizaGanhador(tabuleiro, jogadorGanhou):
    """
    Imprime o tabuleiro e parabeniza o ganhador
    Parâmetros: tabuleiro e jogador que ganhou
    """
    imprimiTabuleiro(tabuleiro)
    # Parabenização invertida pois jogador da vez veio depois da jogada onde a vitória ocorreu
    if jogadorGanhou == "X":
        print("A máquina ganhou!")
    else:
        print("O jogador ganhou! (Não deve acontecer)")

def imprimiTabuleiro(tabuleiro):
    """
    Imprime o tabuleiro utilizando o tabulate para estilização
    Parâmetros: tabuleiro
    """
    print(tabulate(tabuleiro, headers="keys", tablefmt="fancy_grid"))

def confereGanhador(tabuleiro, jogador):
    """
    Confere linhas, colunas e diagonais pelo padrão de vitória
    Parâmetros: tabuleiro
    Retorno: True(Vitória)/False(Sem vitória)
    """
    # Confere Colunas
    if tabuleiro["A"].count("X") == 3 or tabuleiro["A"].count("O") == 3 or \
       tabuleiro["B"].count("X") == 3 or tabuleiro["B"].count("O") == 3 or \
       tabuleiro["C"].count("X") == 3 or tabuleiro["C"].count("O") == 3:
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Linhas
    elif tabuleiro["A"][0] == tabuleiro["B"][0] == tabuleiro["C"][0] and tabuleiro["A"][0] != "" or \
         tabuleiro["A"][1] == tabuleiro["B"][1] == tabuleiro["C"][1] and tabuleiro["A"][1] != "" or \
         tabuleiro["A"][2] == tabuleiro["B"][2] == tabuleiro["C"][2] and tabuleiro["A"][2] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Diagonais
    elif tabuleiro["A"][0] == tabuleiro["B"][1] == tabuleiro["C"][2] or tabuleiro["C"][0] == tabuleiro["B"][1] == tabuleiro["A"][2] and tabuleiro["B"][1] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True
    return False

def confereEmpate(tabuleiro):
    """
    Confere se há espaços disponíveis no tabuleiro
    Parâmetros: tabuleiro
    Retorno: True(Empate)/False(Sem empate)
    """
    if "" not in tabuleiro["A"] and "" not in tabuleiro["B"] and "" not in tabuleiro["C"]:
        imprimiTabuleiro(tabuleiro)
        print("O jogo empatou!")
        return True
    else:
        return False

def confereFim(tabuleiro, jogador):
    """
    Confere se os possiveis finais (vitória de alguma parte) ou empate ocorreram
    Parâmtros: tabuleiro, jogador (que fez a última jogada)
    Retorno: True(Acabou o jogo)/ False(Não acabou o jogo)
    """
    acabou = False
    acabou = confereGanhador(tabuleiro, jogador)
    if not acabou:
        acabou = confereEmpate(tabuleiro)
    return acabou

def confereJogadaCentral(tabuleiro):
    """
        Confere se há jogada inimiga da máquina na posição central
    """
    centro = False

    if tabuleiro["B"][1] == "O":
        centro = True
    
    return centro

def cartadaFinal(tabuleiro):
     # Confere Colunas
    if tabuleiro["A"].count("X") == 2 or \
       tabuleiro["B"].count("X") == 2 or \
       tabuleiro["C"].count("X") == 2 :
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Linhas
    elif tabuleiro["A"][0] == tabuleiro["B"][0] == tabuleiro["C"][0] and tabuleiro["A"][0] != "" or \
         tabuleiro["A"][1] == tabuleiro["B"][1] == tabuleiro["C"][1] and tabuleiro["A"][1] != "" or \
         tabuleiro["A"][2] == tabuleiro["B"][2] == tabuleiro["C"][2] and tabuleiro["A"][2] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Diagonais
    elif tabuleiro["A"][0] == tabuleiro["B"][1] == tabuleiro["C"][2] or tabuleiro["C"][0] == tabuleiro["B"][1] == tabuleiro["A"][2] and tabuleiro["B"][1] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True

def encontrarXganhos(tabuleiro, jogador):
    """
        Encontra X possíveis ganhos de um determinado jogador. Essa função retornará a posição das lacunas das diagonais, colunas e linhas prestes a ganhar.
    """
    listaPossiveisGanhos = {}

    listaPossiveisGanhos.update(retornaPertenceColuna(tabuleiro, jogador))
    listaPossiveisGanhos.update(retornaPertenceLinha(tabuleiro, jogador))
    listaPossiveisGanhos.update(retornaPertenceDiagonal(tabuleiro, jogador))
    return listaPossiveisGanhos
    
def retornaPertenceDiagonal(tabuleiro, jogador):
    """
        Irá retornar um dicionário com os possiveis ganhos nas diagonais
    """
    listaPossiveisGanhos = {}

    # Definindo a primeira e a segunda diagonal
    primeiraDiagonal = {
        "A" : 0,
        "B" : 1,
        "C" : 2
    }

    segundaDiagonal = {
        "C" : 0,
        "B" : 1,
        "A" : 2
    }

    linha,coluna = 0, 0
    contador = 0

    # Navegando entre diagonais
    for chave, index in primeiraDiagonal.items():

        if(tabuleiro[chave][index] ==  jogador):
            contador += 1
        if(tabuleiro[chave][index] == ""):
            linha = chave
            coluna = index   
        if (contador == 2) and linha:    
            listaPossiveisGanhos[f"{linha}"] = coluna 

    contador = 0
    linha,coluna = 0, 0

    for chave, index in segundaDiagonal.items():

        if(tabuleiro[chave][index] ==  jogador):
            contador += 1
        if(tabuleiro[chave][index] == ""):
            linha = chave
            coluna = index   
        if (contador == 2) and linha:    
            listaPossiveisGanhos[f"{linha}"] = coluna 
    
    return listaPossiveisGanhos

def retornaPertenceColuna(tabuleiro, jogador):
    """
        Irá retornar um dicionário com possíveis ganhos em colunas
    """
    listaPossiveisGanhos = {}

    contador = 0
    contadorDeLoops = 0
    linha,coluna = 0, 0

    for chave in tabuleiro.keys():
        for index in range(0,3):
            contadorDeLoops += 1
            if(tabuleiro[chave][index] ==  jogador):
                contador += 1
            if(tabuleiro[chave][index] == ""):
                linha = chave
                coluna = index   
            if(contador == 2) and linha and contadorDeLoops >= 3:    
                listaPossiveisGanhos[f"{linha}"] = coluna
        contador = 0
        contadorDeLoops = 0
        
    return listaPossiveisGanhos

def retornaPertenceLinha(tabuleiro, jogador):
    """
        Irá retornar um dicionário com possíveis ganhos em colunas
    """
    listaPossiveisGanhos = {}

    contador = 0
    contadorDeLoops = 0
    linha,coluna = 0, 0

    for index in range(0,3):
        for chave in tabuleiro.keys():
            contadorDeLoops += 1
            if(tabuleiro[chave][index] == jogador):
                contador += 1
            if(tabuleiro[chave][index] == ""):
                linha = chave
                coluna = index   
            if(contador == 2) and linha and contadorDeLoops >= 3:    
                listaPossiveisGanhos[f"{linha}"] = coluna
        contador = 0
        contadorDeLoops = 0
    
    return listaPossiveisGanhos

def jogadaMaquina(tabuleiro, jogada):
    """
    Processa a jogada que deve ser feita pela máquina
    Parâmetros: tabuleiro, rodada (Contagem de quantas jogadas foram feitas)
    Retorno: tabuleiro
    """
    if jogada == 1:
        tabuleiro["A"][0] = "X" # Inicia as jogadas
    if jogada == 2:
        centro = confereJogadaCentral(tabuleiro)
        if not centro:
            if tabuleiro["A"][2]:     
                tabuleiro["C"][0] = "X"
            elif tabuleiro["A"][1]:
                tabuleiro["B"][0] = "X"
            elif tabuleiro["C"][0]:
                tabuleiro["A"][2] = "X"
            elif tabuleiro["B"][0]:
                tabuleiro["A"][1] = "X"
            else:
                tabuleiro["C"][0] = "X"
        else: 
            tabuleiro["C"][0] = "X" # Jogada para existência de elemento central
        
    if jogada >= 3:
        oAlinhados = encontrarXganhos(tabuleiro, jogador="O")
        xAlinhados = encontrarXganhos(tabuleiro, jogador="X")
        if(xAlinhados):
            linha, coluna = random.choice(list(xAlinhados.items()))
            tabuleiro[linha][coluna] = "X"
        elif(oAlinhados):
            linha, coluna = random.choice(list(oAlinhados.items()))
            tabuleiro[linha][coluna] = "X"
        elif (not confereJogadaCentral(tabuleiro) and jogada == 3 and (not tabuleiro["C"][2] == "O")):
            tabuleiro["B"][1] = "X"    
        
        

    return tabuleiro

# Dicionário para registro do jogo
tabuleiro = {
                " ": ["1", "2", "3"],
                "A": ["", "", ""],
                "B": ["", "", ""],
                "C": ["", "", ""]
            }
# Flag que é acionada para finalizar o jogo
acabou = False
# String para acompanhar qual o jogador da vez
jogador = "X"
# Inteiro para contar em qual rodada estamos
rodada = 0

print("Instruções:\nDigite as coordenadas da sua jogada no formato letra e numero (Exs: 'A 1', 'B 2', 'C 3', etc)\n")
# Loop enquanto jogo não acabar que cicla em jogada da maquina e jogada do usuario com as devidas validações de entrada e fim de jogo
while not acabou:
    rodada += 1
    tabuleiro = jogadaMaquina(tabuleiro, rodada)
    acabou = confereFim(tabuleiro, "X")
    if(acabou):
        break      
    imprimiTabuleiro(tabuleiro)
    tabuleiro = jogada(tabuleiro)
    acabou = confereFim(tabuleiro, "O")
    imprimiTabuleiro(tabuleiro)
  