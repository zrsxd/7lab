import random
def generate_matrix(n, probability=0.3):
    matrix =[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < probability:
                matrix[i][j] = matrix[i][j] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def idk(matrix, visited, node):
    print(node + 1, end=" ")
    visited[node] = True
    for neighbor, connected in enumerate(matrix[node]):
        if connected and not visited[neighbor]:
            idk(matrix, visited, neighbor)


n = 5
matrix = generate_matrix(n)
print("Матрица смежностей")
print_matrix(matrix)

visited = [False] * n 
print("\nОбход в глубину:")
idk(matrix, visited, 0)
