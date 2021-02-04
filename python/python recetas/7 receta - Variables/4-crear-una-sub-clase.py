class Persona:
    def __init__(self, nombre, edad, id):
        self.nombres= nombres
        self.edad = edad
        self.id = id

    def __str__(seft):
        return 'Nombres: {} - Edad: {} - ID:{}'.format(self.nombres, self.edad, self.id)
    
class Empleado(Persona):
    def __init__(self, nombres, edad, id, salario):
        super(Empleado, self).__init__(nombres,edad,id)

        self.salario = salario