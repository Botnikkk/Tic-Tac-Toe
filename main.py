import os

def int_check(num) :
    x = 1
    while x > 0:
        try:
            int(num)
            num = int(num)
            x = -1
        except:
            print("Enter a integer only")
            num = input("\n-")
    return num

def num_check(player_input):
    player_input=int_check(player_input)
    while int(player_input) > 9 or int(player_input) < 1:
        print("Please enter a number between 1 to 9 only")
        player_input = input("\n-")
        player_input=int_check(player_input)
    return int(player_input)


def win_check(pos,player):
    win_comb = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],]

    for combo in win_comb:
        if pos[combo[0]] == pos[combo[1]] == pos[combo[2]]:
            print("*" + "-" *66 + "{} WON".format(player) + "-" *66 + "*")
            return True
    return False


def move_decide(player_num):
    if player_num == "Player1":
        return "X"
    else:
        return "O"


def player_move(player_num, pos):
    global initial_pos
    player_input = input(64* "=" + "{player}  move =".format(player=player_num) + 64* "=" + "\n- ")
    player_input = num_check(player_input)

    if pos[player_input] == player_input:
        pos[player_input] = move_decide(player_num)
        os.system('cls')
        print(142*"=")
        print_board(initial_pos,moves=9)
        print_board(pos)
        winner = win_check(pos, player=player_num)
    else:
        while pos[player_input] != player_input:
            print("Place already taken please choose another place\n")
            player_input = input("-")
            player_input = num_check(player_input)
        pos[player_input] = move_decide(player_num)
        print(142*"=")
        os.system('cls')
        print_board(initial_pos)
        print_board(pos)
        winner = win_check(pos, player=player_num)
    return winner


space = 64 * " "
blank_line = space + "___|___|___\n"


def get_line(line, moves):
    if moves == 9 :
        output = space + " {} | {} | {} ".format(line[0], line[1], line[2]) + "\n"
    else :
        for i in line :
            if type(i) == int :
                line[line.index(i)] = " "
            else :
                continue
        output = space + " {} | {} | {} ".format(line[0], line[1], line[2]) + "\n"
    return output


def print_board(board, moves=0):
    print(get_line(board[1:4], moves)+ blank_line+ get_line(board[4:7], moves)+ blank_line+ get_line(board[7:10], moves))



def startgame():
    os.system('cls')
    player1, player2 = 1, 0
    pos = ["start"]
    global initial_pos
    for i in range(1, 10):
        pos.append(i)
    print(142*"=")
    print_board(board=initial_pos,moves=9)
    moves = 9
    winner = None
    while moves > 0 and not winner:
        if player1 > player2:
            winner = player_move(player_num="Player1", pos=pos)
            moves -= 1
            player2 += 2
        else:
            winner = player_move(player_num="Player2", pos=pos)
            moves -= 1
            player1 += 2

    if moves > 0 and not winner:
        a = None
    elif moves == 0 and not winner:
        print("*" + "-" * 66 + "IT'S A DRAW" + "-" * 66 + "*")

initial_pos=["start",1,2,3,4,5,6,7,8,9]
os.system('cls')
print("\nThis is a multiplayer Tic Tac Toe game. There are two players in this game, Player1 and Player2\nThe Player1 uses the X as it's action and Player2 uses O as it's action\nEnter the number of the the box that you wish to use your action on\nEnter any key/value to start the game !")
start = input("- ")
startgame()

answer = input("\n\nDo you want to play again ?\n* Yes\n* No\n- ").lower()
if answer in ["yes", "no"]:
    while answer == "yes":
        startgame()
        answer = input("\n\nDo you want to play again ?\n* Yes\n* No\n- ").lower()
else:
    while answer not in ["yes", "no"]:
        print("That is not a valid answer")
        answer = input("\n\nDo you want to play again ?\n* Yes\n* No\n- ").lower()
    while answer == "yes":
        startgame()
