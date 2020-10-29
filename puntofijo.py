import math

p0 = 1
limsup = 2
liminf = 1

pn = []
pn.append (p0)
print (pn)
iteracion = 1

while (iteracion <= 10):
    r = pow(pn[iteracion-1], 3) -1 -pn[iteracion-1]
    pn.append(r)
    print (r)
    iteracion = iteracion +1

a = pow (1.3251232001, 3) -1 -1.3251232001
print (a)
