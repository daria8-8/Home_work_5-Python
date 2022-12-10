# Создайте программу для игры в ""Крестики-нолики"".

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
def check_win(board):
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False
def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            player_answer = int(input("Ходит X: "))
            board[player_answer-1] = "X"
        else:
            player_answer = int(input("Ходит O: "))
            board[player_answer-1] = "O"
        count += 1
        if count > 4:
            n = check_win(board)
            if n:
                print(f'Выиграл {n}')
                win = True
                break
        if count == 9:
            print("Ничья!")
            break
    draw_board(board)
board = list(range(1,10))
main(board)