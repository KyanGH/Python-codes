def print_matrix(mat) :
    for row in mat :
        for col in row :
            print(col,end=" ")
        print()
def main() :
    mat = [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ]
    print_matrix(mat)
main()