import math 

p = .7
bandera =0
for i in range (1, 1000):
    a =  p - math.cos(p)
    b =  1 + math.sin(p)
    p = p -a/b

    if ( a < 0.00000000001 and a > 0 ):
        print ("se encontro la raíz en: ", p, "en la iteracion: ", i)
        bandera = 1
        break



if (bandera == 0):
    print ("no se econtro raíz")