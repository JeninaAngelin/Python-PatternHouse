height = int(input())

for i in range(1, height+1):
    
    for j in range(1,height+1):
    
        if(i == j or i == height-j+1):
            print("X",end=" ")
            
        else :
            print("O",end=" ")
    
    print()
    
# Sample Input :- 5
# Output :-
# X O O O X
# O X O X O
# O O X O O
# O X O X O
# X O O O X
