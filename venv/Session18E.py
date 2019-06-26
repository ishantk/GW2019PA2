# Create a ChessBoard of 1s and 0s
"""
0   1   0   1   0   1   0
1   9   1   0   1   0   1
0   1   0   9   0   1   0
1   0   1   0   1   0   1
0   1   0   1   0   1   0
1   0   1   0   1   9   1
0   1   0   1   0   1   0
1   0   1   0   1   0   9
"""
# 1. Use numpy and create a chessboard
import numpy as np

chessBoard = np.zeros((8,8), dtype=int)
# print(chessBoard)

# Use Slicing Method rather than for loop :)
chessBoard[1::2, ::2] = 1
chessBoard[::2, 1::2] = 1

print(chessBoard)

# 2. Ask User to place 4 Queens on ChessBoard
# Where to Place 1st Queen : 1,1
# Where to Place 2nd Queen : 2,3
# Where to Place 3rd Queen : 5,6
# Where to Place 4th Queen : 7,7
# Substitute the index with value 9

queenPosition = input("Where to Place 1st Queen : ")
print(queenPosition, type(queenPosition))


print()
print(chessBoard)

# 3. Validate queens should not be in the same row or same column :)

# 4. Validate queens should not be in the same diagonal(s) :)