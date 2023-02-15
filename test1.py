def PrintMatrix(mat) :
    for row in mat :
        for col in row :
            print(col,end=" ")
        print()
            
def main() :
    mat = [ [1,2,3],
            [1,2,3],
            [1,2,3]]
    PrintMatrix(mat)
main()