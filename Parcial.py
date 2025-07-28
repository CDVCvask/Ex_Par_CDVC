import email
from logging import exception


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
        self.Info = {}
class Evaluation:
    def __init__(self, on_time,team,product,obser):
        self.on_time = on_time
        self.team = team
        self.product = product
        self.obser = obser
        self.Evaluation = {}
    def Avarage(self):
        Total = self.on_time + self.team + self.product
        return Total/3
    def Performance(self,Avarage):
        if Avarage <= 1:
            return "Despedido"
        elif Avarage <7:
            return "Debe mejorar"
        elif Avarage <10:
            return "Satisfactorio"
        else:
            return "Empleado del mes"
class Contact:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
        self.Contact = {}
Empleados = {}
allow = False
Show = False
cont = 0
while allow == False:
    Menu()
    opt = int(input("Selecciona una opcion: "))
    match opt:
        case 1:
            num = int(input("Cuantos empleados desea ingresar? "))
            if num <= 0 or num > 20:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    print(" ")
                    print(f"Empleado {cont+1}:")
                    e_code = f"EMP{cont}"
                    name = input("Ingrese el nombre del empleado: ")
                    department = input("Ingrese el departamento del empleado: ")
                    time = int(input("Ingrese la antiguedad del empleado: "))
                    if time <= 0:
                        print("La cantidad ingresada no es valida")
                    else:
                        on_time = int(input("Del 1 al 10 califique la puntualidad del empleado: "))
                        if on_time <= 0 or on_time > 10:
                            print("La cantidad ingresada no es valida")
                        else:
                            team =int(input("Del 1 al 10 califique el trabajo en equipo del empleado: "))
                            if team <= 0 or team > 10:
                                print("La cantidad ingresada no es valida")
                            else:
                                product = int(input("Del 1 al 10 califique la producción del empleado: "))
                                if product <= 0 or product > 10:
                                    print("La cantidad ingresada no es valida")
                                else:
                                    obser = input("Ingrese alguna observación sobre el empleado: ")
                                    phone = input("Ingrese el telefono del empleado: ")
                                    mail = input("Ingrese el correo del empleado: ")
                                    check_evaluation = Evaluation(on_time,team,product,obser)
                                    Avarage = check_evaluation.Avarage()
                                    Performance = check_evaluation.Performance(Avarage)
                                    cont = cont + 1
                                    Empleados[e_code] = {'Info':{'Nombre':name,'Departamento':department,'Antiguedad':time},
                                                         'Evaluation':{'Puntualidad':on_time,'Trabajo_en_equipo':team,'Producción':product,'Observaciones':obser,
                                                                       'Promedio':Avarage,'Desempeño':Performance},
                                                         'Contact':{'Correo':mail,'Telefono':phone}}
                                    Show = True
        case 2:
            cont1 = 1
            if Show == False:
                print("No hay ningún dato que mostrar")
            else:
                for code,value in Empleados.items():
                    print(" ")
                    print(f"Empleado {cont1}:")
                    print(f"Código de empleado: {code}")
                    for key, val in value['Info'].items():
                        print(f"{key} del empleado: {val}")
                    for key, val in value['Evaluation'].items():
                        print(f"{key} del empleado: {val}")
                    for key, val in value['Contact'].items():
                        print(f"{key} del empleado: {val}")
                cont1 = cont1 + 1
        case 3:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción ingresada no es valida")
