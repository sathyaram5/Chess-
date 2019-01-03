
# coding: utf-8

# In[ ]:


###### M = 1.6

#Defining Knight's possible moves                       
def getKnightMoves(x0, y0):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)] #setting coordinates of deltas
    validPositions = []
    for (x, y) in deltas:
        xCandidate = x0 + x
        yCandidate = y0 + y
        if 0 <=xCandidate < 8 and 0 <=yCandidate < 8:   #filtering within extreme cases
            validPositions.append([xCandidate, yCandidate])
        
    return(validPositions) # returns available positions


    
# Bishop's possible moves :
def getAllMovesBishop(x1,y1):
    deltasb=[]
    validPositionsb = []
    for i in range(0,8):
            val = ([i,i]) #all diagonal coordinates
            deltasb.append(val)
    #filtering under conditions of bishop movement :        
    for (x,y) in deltasb:
        xCandidateb = x1 + x
        yCandidateb = y1 + y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                    break
            
    for (x,y) in deltasb:
        xCandidateb = x1 - x
        yCandidateb = y1 - y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    for (x,y) in deltasb:
        xCandidateb = x1 + x
        yCandidateb = y1 - y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break


    for (x,y) in deltasb:
        xCandidateb = x1 - x
        yCandidateb = y1 + y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    final = []
    for i in validPositionsb:
        if([x1,y1]!= i):
            final.append(i)
    #return the list to the next function
    return final

#Possible positions of Rook
def getAllMovesRook(x1,y1):
    deltasb=[]
    validPositionsb = []
    
    # Filtering according to rook positions in chess_matrix with respect to coordinates
    
    for i in range(-1,8):
            val = ([i,i])
           # val.append[0,0];
            deltasb.append(val)
            
    for (x,y) in deltasb:
        xCandidateb = x1
        yCandidateb = y1 + y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    for (x,y) in deltasb:
        xCandidateb = x1
        yCandidateb = y1 - y
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and yCandidateb!=y1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    for (x,y) in deltasb:
        xCandidateb = x1 + x
        yCandidateb = y1
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    for (x,y) in deltasb:
        xCandidateb = x1 - x
        yCandidateb = y1
        if 0 <= xCandidateb <= 7 and 0 <= yCandidateb <= 7 and xCandidateb!=x1 :
            if chess_matrix[xCandidateb][yCandidateb]!=1:
                validPositionsb.append([xCandidateb, yCandidateb])
            else:
                break

    final = []
    for i in validPositionsb:
        if([x1,y1]!= i):
            final.append(i)
    #return the list to the next function
    return final


#Possibe moves of queen
def getAllMovesQueen(x1,y1):
     moves = [] #  Possible queen moves is both Bishop and Rook
     a = getAllMovesBishop(x1,y1);   
     b = getAllMovesRook(x1,y1);
     moves = a+b;

     return moves 


#Possible pawn moves   
def getAllMovesPawn(x1,y1):
    
    #Setting up possible delta coordinates
    if(x1=='1'):
        deltas=[(1,0),(1,-1),(1,1),(0,2)]
    else:
         deltas = [(1,0), (1,-1), (1,1)]
    
    validPositions = []
    for (x, y) in deltas:
        xCandidate = x1 + x  
        yCandidate = y1 + y
        if 0 <= xCandidate < 8 and 0 <= yCandidate < 8:
            validPositions.append([xCandidate, yCandidate])
    return(validPositions)
    
def getKingMoves(xk,yk):
   
    deltas = [(0,1), (-1,1), (1,1),(-1,-1),(-1,+1),(-1,0),(1,0),(0,-1)]
    validPositions = []
    for (x, y) in deltas:
        xCandidate = xk + x
        yCandidate = yk + y
        if 0 <=xCandidate < 8 and 0 <=yCandidate < 8:
            validPositions.append([xCandidate, yCandidate])
        
    return(validPositions)


def HashMap(res):
    map = {}
    test = []
    po = []
    i=0
    for i in res:
        if(chess_matrix[i[0]][i[1]]!=1):
             test.append(i)
    
    res=test
    for i in res:
        if i not in po:
            po.append(i)
    res = po
    i=0
    for i in range(len(res)):
        a = res[i][0]
        b = res[i][1]
        if chess_matrix[a][b] != 1:
            map[i] = res[i]
            
    while True:
        options=map.keys()
        sorted(options)
        for entry in options: 
            x = map[entry][0] + 1
            y = chr(map[entry][1] + 97)
            if(chess_matrix[map[entry][0]][map[entry][1]]==0):
                print (entry,'Position', x,y)
                test.append(entry)
        if(len(test)==0):
            print('No position is available')
            break
        else:
            inputt = input('Please Select the position number you want to move:')
            if inputt == '' or inputt.isalpha():
                print('You have not entered anything')
            elif len(inputt)>2:
                print('Wrong Input')
            elif inputt is None:
                print('Wrong Input')
            elif int(inputt) in map.keys():
                inputt =int(inputt)
                a = map[inputt][0] 
                b = map[inputt][1]
                if chess_matrix[a][b] == 1:
                    print('Wrong Input')
                else:
                    chess_matrix[a][b] = 1
                    val1 = a + 1
                    val2 = chr(b + 97)
                    print('Finally selected row details: ')
                    print('row: ',val1,' col: ',val2)
                    print('Thank You!')
                    print('\n')
                    break
            else:
                print('Please Select a Proper Option')



def get_position(): #Gets user input for position based on number and letter -ex: 3a
    while True:
        position = input('Enter Position: ')
        if position == '':
            print('Sorry, Empty input')
        elif position is not None:
            position = position.lower()
            position.split()
            output = []
            if(len(position) == 1):
                print('Sorry,Invalid input')
            elif (position[1].isdigit() or position.isalpha()): 
                print('Sorry,Invalid input')
            elif (int(position[0]) < 0 or int(position[0]) > 8):
                print('Sorry,Invalid input')
            elif ((ord(position[1]) - 96) > 8):
                print('Sorr,Invalid input')
            else:    
                for character in position:
                    if character.isdigit():
                        output.append(int(character)-1)
                    else:
                        number = ord(character) - 96
                        output.append(number-1)
                        if chess_matrix[output[0]][output[1]] == 1: #Checks if occupied or not using flag
                            print('Sorry, Position is already filled')
                        else:
                            return output
        else:
            print('Enter a Proper Value')
    
def main():
     print("")
chess_matrix = [[0 for x in range(8)] for y in range(8)] #boundary ranges
print('The Following is the chess Board Program')
print('All 8 rows are named using numbers [1-8]')
print('All 8 columns are named using numbers [a-h]')
print('The Positions are named as 1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h')
print('The Positions are named as 2a, 2b, 2c, 2d, 2e, 2f, 2g, 2h')
print('---------------------------------------------------------')
print('The Positions are named as 8a, 8b, 8c, 8d, 8e, 8f, 8g, 8h')
print('******Lets Start the Game!!!******')
print('You can select one of the following 1.Rook 2.Knight 3.Bishop 4.Queen 5.King 6.Pawn')
print('\n')

while True: # Loops until False
    sel = input('Enter the Piece name' + ' ' )   #Receives Piece of choice
    if sel == 'Rook' or sel == 'rook':
        inp_pos = get_position() #Gets input positons
        possible_moves = getAllMovesRook(inp_pos[0],inp_pos[1]) #Calls the corresponding piece for possible moves
        HashMap(possible_moves) # Prints unoccupied possibilities
        dec = input('Do you want to continue? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N'  or dec== 'no' :
            break;
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again...')
       
        
    elif sel == 'Knight' or sel == 'knight':
        inp_pos = get_position()                        #Gets input positons
        possible_moves = getKnightMoves(inp_pos[0],inp_pos[1])#Calls the corresponding piece for possible moves
        HashMap(possible_moves)
        dec = input('Do you want to continue? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N'  or dec== 'no':
            break
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again...')
        
    elif sel == 'Bishop' or sel == 'bishop':
        inp_pos = get_position()            #Gets input positons
        possible_moves = getAllMovesBishop(inp_pos[0],inp_pos[1])#Calls the corresponding piece for possible moves
        HashMap(possible_moves)
        dec = input('Do you want to continue? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N'  or dec== 'no':
            break
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again...')
        
    elif sel == 'Queen' or sel == 'queen':
        inp_pos = get_position()         #Gets input positons
        possible_moves = getAllMovesQueen(inp_pos[0],inp_pos[1])#Calls the corresponding piece for possible moves
        HashMap(possible_moves)
        dec = input('Do you want to continue.? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N'  or dec== 'no':
            break
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again.....')
        
    elif sel == 'King' or sel == 'king':
        inp_pos = get_position()          #Gets input positons
        possible_moves = getKingMoves(inp_pos[0],inp_pos[1])#Calls the corresponding piece for possible moves
        HashMap(possible_moves)
        dec = input('Do you want to continue.? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N'  or dec== 'no':
            break;
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again...')
            
    elif sel == 'Pawn' or sel == 'pawn':
        inp_pos = get_position()           #Gets input positons
        possible_moves = getAllMovesPawn(inp_pos[0],inp_pos[1])#Calls the corresponding piece for possible moves
        HashMap(possible_moves)
        dec = input('Do you want to continue.? [yes/no]')
        if dec == 'No' or dec == 'n' or dec == 'N' or dec== 'no':
            break
        
        elif dec == 'Yes' or 'y' or 'Y':
            print('Playing the Game Again...')
    else:               #Checks for incorrect input, if yes, goes back again
            print('You have entered incorrectly, please enter properly') 
    
    
main()

