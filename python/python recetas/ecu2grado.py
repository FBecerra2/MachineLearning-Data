from math import sqrt 
A = int(input("Ingrese A\n"))
B = int(input("Ingrese B\n"))
C = int(input("Ingrese C\n"))

if ((B**2-4*A*C)) <= 0 :
        print("La Raiz va negativa")
else:
        x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
        xi = (-B-sqrt(B**2-(4*A*C)))/(2*A)
        print("Las x1 y x2 son:", x1 ,xi)