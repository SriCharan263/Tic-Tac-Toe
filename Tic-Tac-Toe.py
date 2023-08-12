def choose_player_mark():
    P1='wrong'
    while P1!='X' and P1!='O':
        P1=input('Player one please select "X" or "O" as your mark ').upper()
        if P1== 'X':
            P2='O'
        elif P1=='O': 
            P2='X'
        else:
            print('Sorry, select any one of "X" or "O"')
    print(f'Player-1 is {P1} and Player-2 is {P2}')
    return P1,P2
    
def current_table():
    
    print('   |   |   ')
    print(f' {table[0][0]} | {table[0][1]} | {table[0][2]} ')
    print('------------')
    print('   |   |   ')
    print(f' {table[1][0]} | {table[1][1]} | {table[1][2]} ')
    print('------------')
    print('   |   |   ')
    print(f' {table[2][0]} | {table[2][1]} | {table[2][2]} ')
    
    

def position_to_mark(table):
    positions_available = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print(*positions_available,sep='\n')
    
    while True:
        a = input('Choose position from 1 to 9: ')
        if a.isdigit() and 1 <= int(a) <= 9:
            a = int(a)
            row = (a - 1) // 3
            col = (a - 1) % 3
            if table[row][col] == ' ':
                return row, col
            else:
                print('Sorry, this position is unavailable. Please select another position.')
        else:
            print('Invalid input. Please enter a number from 1 to 9.')
            
def replacement(table, row, col, user_input):
    table[row][col] = user_input
    
    
def check_win(table):
    win=[[table[0][0],table[1][1],table[2][2]],[table[0][1],table[1][1],table[2][1]],[table[0][2],table[1][1],table[2][0]],[table[1][0],table[1][1],table[1][2]],[table[0][0],table[0][1],table[0][2]],[table[2][0],table[2][1],table[2][2]],[table[0][0],table[1][0],table[2][0]],[table[0][2],table[1][2],table[2][2]]]
    for condition in win:
        if condition==['X','X''X'] or condition==['O','O','O']:
            return True
        
    return False
    
        
def board_full(table):
    count=0
    for e in table:
        if ' ' not in e:
            count+=1
    if count==3:
        return True
    else:
        return False
        
    
print(' Welcome to Tic Tac Toe !!!')
table=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
game_on=True
while game_on:
    P1,P2=choose_player_mark()
    i=0
    while i<9:
        
        current_table()
        chance_to_play=P1 if i % 2 == 0 else P2
        print(f'Chance of {chance_to_play}')
        row,col=position_to_mark(table)
        replacement(table,row,col,chance_to_play)
        
        
        if check_win(table):
            
            current_table()
            print(f'{chance_to_play} wins')
            print('X------X------X')
            print(' Game Over ')
            break
            
        if board_full(table):
            
            current_table()
            print(" It's a draw ")
            print('X------X------X')
            print(' Game Over ')
        i+=1
            
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        game_on = False