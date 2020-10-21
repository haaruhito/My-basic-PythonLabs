board = []
EMPTY = 'a'
for i in range(8):
    row = [EMPTY for i in range(8)] #If I understood right, it completely completes this statement first. The last output then go for above command. 
    board.append(row)
    print(board) #It print 8 times adding 'a' in the list, 'board' as the range is from 0 to 7

print("OR--See the difference") #It prints the final result. 
print(board)