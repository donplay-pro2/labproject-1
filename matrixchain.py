def printParenthesis(m, j, i ):
    if j == i:
        print(str(65) + str(j), end = "") #when at diagonals just print the matrix name
        return;
    else:
        print("(", end = "") #opening parenthesis
        printParenthesis(m, m[j][i] - 1, i) # evaluating between i to k
        printParenthesis(m, j, m[j][i])   # evaluating between k+1 to j combinning it we get i to j
        print (")", end = "" ) # closing paranthesis
def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+ 1):
            j = i + l-1
            m[i][j] = float('Inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    m[j][i] = k + 1
    return m

arr = [int(i) for i in input().split()]
n = len(arr)-1
m = MatrixChainOrder(arr, n)
print("The parenthesis will be like: ",end="")
printParenthesis(m,n-1,0)
print("\nThe minimum cost of multiplying matrices: ",m[0][n-1])
