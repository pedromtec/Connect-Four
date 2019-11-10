from board import Board

def score_janela(janela, peca):
    score = 0
    opn_peca = 1 if peca == 2 else 2
    if janela.count(peca) == 4:
        score += 100
    elif janela.count(peca) == 3 and janela.count(0) == 1:
        score += 10
    elif janela.count(peca) == 2 and janela.count(0) == 2:
        score += 4
    if janela.count(opn_peca) == 3 and janela.count(0) == 1:
        score -= 10
    
    return score

def score_position(board):
    peca = Board.OPONENTE
    score = 0
    meio = len(board[0]) // 2
    NUM_LIN = len(board)
    NUM_COL = len(board[0])

    for i in range(NUM_LIN):
        if board[i][meio] == peca:
            score += 1
    score *= 10
    for i in range(NUM_LIN):
        for j in range(NUM_COL-3):
            janela = [board[i][j], board[i][j+1], board[i][j+2], board[i][j+3]]
            score += score_janela(janela, peca)
    for j in range(NUM_COL):
        for i in range(NUM_LIN-3):
            janela = [board[i][j], board[i+1][j], board[i+2][j], board[i+3][j]]
            score += score_janela(janela, peca)
    for i in range(NUM_LIN-3):
        for j in range(NUM_COL-3):
            janela = [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]]
            score += score_janela(janela, peca)
    for i in range(NUM_LIN-3):
        for j in range(3, NUM_COL):
            janela = [board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3]]
            score += score_janela(janela, peca)
    return score