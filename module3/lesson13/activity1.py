theBoard={'7':'','8':'','9':'',
          '4':'','5':'','6':'',
          '1':'','2':'','3':''
          }
board_keys=[]
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board[' 4 ']+'|'+board[' 5']+'|'+board['  6'])
    print('-+-+-')
    print(board['1']+'|'+board[' 2']+'|'+board['3 '])

    #now we'll write the main function which has all the gameplay functionality
    def game():
        turn='X'
        count=0
         
        for i in ramge(10):
            printBoard(theBoard)
            print("It's yourn turn,"+turn+".Move to which place?")
            move=input()
            if theBoard[move]=='':
                theBoard[move]=turn
                


    


