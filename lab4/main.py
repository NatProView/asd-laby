from colorama import Fore
from colorama import Style

# napisane na podstawie pseudokodu dr Pączkowskiego oraz przykładu na stronie www.geeksforgeeks.org

def lcs(X, Y, m, n):

    # przygotowuje wielkość listy L na podstawie długości dwóch ciągów znaków
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
 

    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])


    index = L[m][n]
    
    lcs = [""] * (index + 1)
    lcs[index] = ""
 
    i = m
    j = n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # wyswietl tabelke pomocnicza 
    # TODO dodaj zaznaczanie indeksow np przez krotke albo obiekt z boolem

    for i in range(len(L)):
        print(L[i])

    print ("LCS of " + X + " and " + Y + " is " + "".join(lcs))


print("Would you like to compare two strings from files or provide them yourself in the terminal?")
temp = int(input("1 - from files\n2 - provide them yourself\n"))
if temp == 1:
    # założyłem, że można hardcode'ować nazwy plików
    with open('x', 'r') as x_file, open('y', 'r') as y_file:
        X = x_file.read()
        Y = y_file.read()
        m = len(X)
        n = len(Y)
if temp == 2:
    X = str(input("Provide first string:\n"))
    Y = str(input("Provide second string:\n"))
    m = len(X)
    n = len(Y)

lcs(X, Y, m, n)