#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    '''scripts to rotate nxn 2D matrix clockwise
    Return: Nothing '''
    
  # step-1: transpose the matrix
  for i in range(len(matrix)):
    for j in range(i, len(matrix)):
      matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

  # step-2: reverse the matrix
  N=len(matrix)
  for i in range(N//2):
    for j in range(N):
      matrix[j][i],matrix[j][N-1-i]=matrix[j][N-1-i],matrix[j][i]
