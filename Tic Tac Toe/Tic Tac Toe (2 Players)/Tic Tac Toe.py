import random

index_board = [" "," "," "," "," "," "," "," "," "]

def display_board(putsignpos, sign):
    if putsignpos == sign == " ":
        print(index_board[0] + "|" + index_board[1] + "|" +index_board[2] + "\n" +
              "-"+ " " + "-" + " " + "-" + "\n" +
              index_board[3] + "|" + index_board[4] + "|" + index_board[5] + "\n" +  
              "-"+ " " + "-" + " " + "-"+ "\n" + 
              index_board[6] + "|" + index_board[7] + "|" + index_board[8]  )
    else:
        index_board[putsignpos] = sign 
        print(index_board[0] + "|" + index_board[1] + "|" +index_board[2] + "\n" +
              "-"+ " " + "-" + " " + "-" + "\n" +
              index_board[3] + "|" + index_board[4] + "|" + index_board[5] + "\n" +  
              "-"+ " " + "-" + " " + "-"+ "\n" + 
              index_board[6] + "|" + index_board[7] + "|" + index_board[8]  )
    return index_board

def random_player():
    player_list = ["player1","player2"]
    player = random.choice(player_list)
    return player

def check_win(index_board , player , i):
    if (index_board[0] == index_board[1] == index_board[2] or
        index_board[3] == index_board[4] == index_board[5] or
        index_board[6] == index_board[7] == index_board[8] or
        index_board[0] == index_board[3] == index_board[6] or
        index_board[1] == index_board[4] == index_board[7] or
        index_board[2] == index_board[5] == index_board[8] or
        index_board[0] == index_board[4] == index_board[8] or
        index_board[2] == index_board[4] == index_board[6] ):

        print("You Won "+ player)
        quit()

    elif i>7 and not(index_board[0] == index_board[1] == index_board[2] or
                    index_board[3] == index_board[4] == index_board[5] or
                    index_board[6] == index_board[7] == index_board[8] or
                    index_board[0] == index_board[3] == index_board[6] or
                    index_board[1] == index_board[4] == index_board[7] or
                    index_board[2] == index_board[5] == index_board[8] or
                    index_board[0] == index_board[4] == index_board[8] or
                    index_board[2] == index_board[4] == index_board[6] ):

        print("Match Tie")
        quit()

def tic_tac_toe():
    play = random_player()
    blank_string = " "
    display_board(blank_string , blank_string)
    if play == "player1":
        sign = "X"
        # sign1 = "O"
        # play2 = "player2"
        print("Player1(X) get the first chance")
    else:
        sign = "O"
        # sign1 = "X"
        # play2 = "player1"
        print("Player2(O) get the first chance")
    i = 0
    while i<9:
        if play == "player1":
            print(play + "Turn")
            putsignpos = int(input("At which position you want to put "+ sign + " :"))
            display_board(putsignpos-1 , sign)
            if i>=5:
                check_win(index_board , play , i)
            play = "player2"
            sign = "O"
            i = i + 1
        else:
            print(play + "Turn")
            putsignpos = int(input("At which position you want to put "+ sign + " :"))
            display_board(putsignpos-1 , sign)
            if i>=5:
                check_win(index_board , play , i)
            play = "player1"
            sign = "X"
            i = i + 1 

tic_tac_toe()
