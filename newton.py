import math

p=1
n=2
bandera = 0

print ("se recibe la función x**3 -x -1    en C[1,2]")
print ("hallar un punto fijo  tal que f(x) = 0 en C[1,2]")

for i in range (1, 10):
    a = p*p*p - p -1
    b = 3*p*p -1
   # print (a,b)
    if (a > 0 and a < 0.000000000000001):
        print ("se enonctro raiz en: " ,p, "en la iteracion:", i)
        bandera =1
        break
    p = p -a/b
    #print (p)

if (bandera == 0):
    print ("no se econtro raíz")
    