import heuristica
from board import Board 
import random
import math

chamadas_recursivas = 0

#Minimax com Alpha Beta
def minimax(board, depth, alpha, beta, maximazing_player):
    global chamadas_recursivas
    chamadas_recursivas += 1
    if board.winner:
        if board.winner == Board.PLAYER:
            return None, -math.inf
        else:
            return None, math.inf

    if depth == 0:
        return None, heuristica.score_position(board.board)

    colunas_validas = board.get_valid_positions()
    if colunas_validas:
        best_col = random.choice(colunas_validas)
    if maximazing_player:
        score = -math.inf
        for col in colunas_validas:
            board.drop_piece(col)
            new_score = minimax(board, depth-1,alpha, beta,False)[1]
            board.back_state()
            if new_score > score:
                score = new_score
                best_col = col
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return best_col, score
    else:
        score = math.inf
        for col in colunas_validas:
            board.drop_piece(col)
            new_score = minimax(board, depth-1, alpha, beta, True)[1]
            board.back_state()
            if new_score < score:
                score = new_score
                best_col = col
            beta = min(beta, score)
            if alpha >= beta:
                break
        return best_col, score

def get_best_move(board):
    global chamadas_recursivas
    chamadas_recursivas = 0
    resp = minimax(board, 6, -math.inf, math.inf, True)
    return resp, chamadas_recursivas


