# .Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking 
# for n-queens problem
print("Enter the number of queens : ")
N = int(input())
board =[[0]*N for _ in range(N)]

def attack(i, j):
    for k in range(0, N):
        if(board[i][k]==1 or board[k][j]==1):
            return True
    for k in range(0, N):
        for l in range(0, N):
            if((k+l == i+j) or (k-l==i-j)):
                if board[k][l] == 1:
                    return True
            
    return False
    
def nqueen(n):
    for i in board:
        print(i)
    print('/n')
    if n==0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if(not(attack(i, j)) and board[i][j]!=1):
                board[i][j] = 1
                if nqueen(n-1) == True:
                    return True
                board[i][j] = 0
        
    return False

nqueen(N)

for i in board:
    print(i)



# N = int(input("Enter number of queens: "))

# # Function to print the solution
# def printsol(board):
#     for row in board:
#         for cell in row:
#             print(cell, end=" ")
#         print()

# # Function to check if a queen can be placed safely at board[row][col]
# def is_safe(board, row, col):
#     # Check if there is a queen in the same row
#     for i in range(col):
#         if board[row][i] == 1:
#             return False
    
#     # Check upper diagonal on the left side
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
    
#     # Check lower diagonal on the left side
#     for i, j in zip(range(row, N, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
    
#     return True

# # Recursive function to solve N Queen problem
# def solveNQUtil(board, row):
#     # All queens are placed
#     if row >= N:
#         return True
    
#     # Consider this row and try placing a queen in all columns one by one
#     for i in range(N):
#         if is_safe(board, i, row):
#             board[i][row] = 1
#             # Recur to place rest of the queens
#             if solveNQUtil(board, row + 1):
#                 return True
#             # If placing queen in board[i][row] doesn't lead to a solution then backtrack
#             board[i][row] = 0
    
#     # If queen can't be placed in any row of this column, then return false
#     return False

# # Main function to solve N Queen problem
# def solveprob():
#     board = [[0 for _ in range(N)] for _ in range(N)]
#     if not solveNQUtil(board, 0):
#         print("Solution does not exist")
#         return False
#     printsol(board)
#     return True

# # Driver code
# print()
# print(f"Solution for {N} Queen problem is")
# solveprob()










## time complexity is N^N. 


# print("Enter the number of queens : ")
# N = int(input())  # Input the number of queens
# board =[[0]*N for _ in range(N)]  # Create an empty chessboard of size N x N

# def attack(i, j):
#     # Check if there's any queen in the same row or column
#     for k in range(0, N):
#         if(board[i][k]==1 or board[k][j]==1):
#             return True
#     # Check if there's any queen diagonally attacking
#     for k in range(0, N):
#         for l in range(0, N):
#             if((k+l == i+j) or (k-l==i-j)):
#                 if board[k][l] == 1:
#                     return True
#     return False

# def nqueen(n):
#     for i in board:  # Print the board
#         print(i)
#     print('/n')
#     if n==0:  # If all queens are placed
#         return True
#     for i in range(0, N):  # Iterate through each row
#         for j in range(0, N):  # Iterate through each column
#             # If it's safe to place a queen in this cell
#             if(not(attack(i, j)) and board[i][j]!=1):
#                 board[i][j] = 1  # Place the queen
#                 # Recursively place remaining queens
#                 if nqueen(n-1) == True:
#                     return True
#                 board[i][j] = 0  # Backtrack if placement leads to failure
#     return False

# nqueen(N)  # Start the N-Queen problem solving

# for i in board:  # Print the final board configuration
#     print(i)
