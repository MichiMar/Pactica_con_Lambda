class Empleado:
     def __init__(self, nombre, cargo, salario):

         self.nombre=nombre
         self.cargo=cargo
         self.salario=salario
    def __str__(self):

        return "Nombre:{}, Puesto:{}, Salario:${}".format(self.nombre, self.cargo, self.salario)


lista_empleados=[
    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Presidenta", 8450),
    Empleado("Antonio", "Administrativo", 7500),
    Empleado("Sara", "Director", 3570),
    Empleado("Mario", "Plomero", 1000)
]

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado

comision_empleados=map(calculo_comision, lista_empleados)

for empleado in comision_empleados:
    print(empleado)

