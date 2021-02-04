def calcular_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n *  calcular_factorial(n-1)

print(calcular_factorial(5))

