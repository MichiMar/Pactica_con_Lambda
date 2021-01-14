# def numero_par(num):
#     if num % 2==0:
#         return True
'''
numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))'''

class Empleado:
     def __init__(self, nombre, cargo, salario):

         self.nombre=nombre
         self.cargo=cargo
         self.salario=salario
    def __str__(self):

        return "Nombre:{}, Puesto:{}, Salario:${}".format(self.nombre, self.cargo, self.salario)


Lista_empleados=[
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidenta", 84560),
    Empleado("Antonio", "Administrativo", 7500),
    Empleado("Sara", "Director", 35751),
    Empleado("Mario", "Plomero", 1000000)
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, Lista_empleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)