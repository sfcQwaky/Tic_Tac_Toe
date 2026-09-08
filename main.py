from email import message

line_1 =[" "," "," "]
line_2 =[" "," "," "]
line_3 =[" "," "," "]

show_1=["1A","1B","1C"]
show_2=["2A","2B","2C"]
show_3=["3A","3B","3C"]


def print_board(first, second, third):
    row_1 = first
    row_2 = second
    row_3 = third
    print(f" {row_1[0]} | {row_1[1]} | {row_1[2]} \n"
          "-----------\n"
          f" {row_2[0]} | {row_2[1]} | {row_2[2]} \n"
          "-----------\n"
          f" {row_3[0]} | {row_3[1]} | {row_3[2]} ")


def win_check(row1,row2,row3):
    #first for loop is checking does each row
    win = False
    message = ""
    for row in (row1,row2,row3):
        if row[0]==row[1]==row[2]:
            if row[0]=="X":
                win = True
                message = "Player 1 wins!"
            elif row[0]=="O":   #I can't use else because all three can have empty value
                win = True
                message = "Player 2 wins!"

    if (row1[0]=="X" and row2[0]=="X" and row3[0]=="X") or (row1[1]=="X" and row2[1]=="X" and row3[1]=="X") or (row1[2]=="X" and row2[2]=="X" and row3[2]=="X"):
        win = True
        message = "Player 1 wins!"
    elif (row1[0]=="O" and row2[0]=="O" and row3[0]=="O") or (row1[1]=="O" and row2[1]=="O" and row3[1]=="O") or (row1[2]=="O" and row2[2]=="O" and row3[2]=="O"):
        win = True
        message = "Player 2 wins!"
    elif (row1[0]=="X" and row2[1]=="X" and row3[2]=="X") or (row1[2]=="X" and row2[1]=="X" and row3[0]=="X"):
        win = True
        message = "Player 1 wins!"
    elif (row1[0]=="O" and row2[1]=="O" and row3[2]=="O") or (row1[2]=="O" and row2[1]=="O" and row3[0]=="O"):
        win = True
        message = "Player 2 wins!"
    return win, message


stop=False
print("Here is a grid example for entering X or O")
print_board(show_1,show_2,show_3)
var_2 = 0
while stop==False:
    if var_2 % 2==0:
        var_3="X"
    else:
        var_3="O"
    var_1=input(f"Player {var_3}, please enter grid value: ")

    if var_1=="1A":
        line_1[0]=var_3
    elif var_1=="1B":
        line_1[1] = var_3
    elif var_1=="1C":
        line_1[2] = var_3
    elif var_1=="2A":
        line_2[0] = var_3
    elif var_1=="2B":
        line_2[1] = var_3
    elif var_1=="2C":
        line_2[2] = var_3
    elif var_1=="3A":
        line_3[0] = var_3
    elif var_1=="3B":
        line_3[1] = var_3
    elif var_1=="3C":
        line_3[2] = var_3

    print_board(line_1, line_2, line_3)

    win, message= win_check(line_1, line_2, line_3)

    if message!="":
        print(f"Game Over! {message}")
    stop = win

    var_2+=1
