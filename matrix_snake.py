def snake(mat):
    for i in range(len(mat) - 1):
        for j in range(len(mat[i]) - 2):
            if j % 2 == 1 :
                if mat[i][j] < mat[i+1][j] or mat[i][j] > mat[i][j+2] :
                    return False
            elif mat[i][j] > mat[i+1][j] or mat[i][j] > mat[i][j+2] :
                return False
    return True
    
def printmatrix(mat) :
    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            print(mat[i][j],end=" ")
        print()
def main():
    mat = [[-1,8,9,16,17],[2,7,10,15,18],[3,6,11,14,19],[4,5,12,13,28]]
    printmatrix(mat)
    print(snake(mat))
main()