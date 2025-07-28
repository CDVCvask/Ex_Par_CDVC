def Menu():
    print("Menu Principal")
    print("1.Agregar empleados")
    print("2.Mostrar empleados")
    print("3.Salir")
class Emloyee:
    def __init__(self, name,department,time):
        self.name = name
        self.department = department
        self.time = time
        self.evaluation = {}
class Evaluation:
    def __init__(self, on_time,team,product,obser):
        self.on_time = on_time
        self.team = team
        self.product = product
        self.obser = obser
class Contact:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

