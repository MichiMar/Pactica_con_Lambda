'''def area_triangulo(base, altura):
    return (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2)'''

'''area_triangulo=lambda base,altura: (base*altura)/2
# una funcion lambda no tiene bucles o condicnioales, son calculos los que regresa
# la funcion lambda es una funcion anonima, no tiene nombre
# en los libros se conoce como funciones on te go, on demand, online

print(area_triangulo(7,5))
print(area_triangulo(9,6))

# o tambien se pueden pedir como en el primer ejemplo
triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2)'''

al_cubo=lambda numero:pow(numero, 3) #El primero es la base y el segundo es el exponente
al_cubo=lambda numero:pow(numero**3)

print(al_cubo(13))