import random
board = [' ' for _ in range(9)]

def create_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def pMove():
    run = True
    while run:
        move = input("Select a position[1-9] : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_free(move):
                    run = False
                    insert_letter('X',move)
                else:
                    print("Sorry, space already occupied!")
            else:
                print("please type valid position!")
        except:
            print("please type a number!")
def ai_move(diff):
    if diff == "easy":
        easy_ai()
    elif diff == "normal":
        normal_ai()
    else:
        best_ai_move()
def easy_ai():
    #choosing moves randomly
    available_pos = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_pos)
    insert_letter('0',move+1)
def normal_ai():
    #AI is using minimax 70% of the time and 30% of time it is choosing randomly
    if random.random() < 0.3:
        easy_ai()
    else:
        best_ai_move()
def best_ai_move():
    best_score = -1000
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = '0'
            score = minimax(board,0,False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    insert_letter('0',best_move+1)

def space_free(pos):
    return board[pos-1]==' '
def insert_letter(letter,pos):
    board[pos-1] = letter
def is_full():
    return ' ' not in board
def is_winner(letter):
    winning_state = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for combo in winning_state:
        if board[combo[0]]==board[combo[1]]==board[combo[2]]==letter:
            return True
    return False
def minimax(board,depth,is_maximizing):
    if is_winner('0'):
        return 10
    elif is_winner('X'):
        return -10
    elif is_full():
        return 0
    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i]==' ':
                board[i]='0'
                score = minimax(board,depth+1,False)
                board[i] = ' '
                best_score = max(score,best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board,depth+1,True)
                board[i] = ' '
                best_score= min(score,best_score)
        return best_score

#Driver function for game
def play_game():
    print("TIC TAC TOE!")
    print("----------------------------")
    difficulty = ""
    while difficulty not in ["easy","normal","hard"]:
        difficulty = input("Select difficulty(easy,normal,hard) : ").lower()
    create_board()
    while not is_full():
        pMove()
        create_board()
        print()
        if is_winner('X'):
            print("----------------------")
            print("Player wins!")
            break
        ai_move(difficulty)
        create_board()
        print()
        if is_winner('0'):
            print("----------------------")
            print('AI wins!')
            break
    if is_full():
        print("----------------------")
        print("It\'s a tie!")

if __name__=="__main__":
    play_game()