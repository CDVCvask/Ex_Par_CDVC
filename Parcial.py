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
allow = False
cont = 0
while allow == False:
    Menu()
    opt = int(input("Selecciona una opcion: "))
    match opt:
        case 1:
            num = int(input("Cuantos empleados desea ingresar?"))
            if num <= 0 or num > 20:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    e_code = f"EMP{cont}"
                    name = input("Ingrese el nombre del empleado: ")
                    department = input("Ingrese el departamento del empleado: ")
                    time = input("Ingrese la antiguedad del empleado: ")
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
                                    obser = int(input("Ingrese alguna observación sobre el empleado: "))
                                    phone = input("Ingrese el telefono del empleado: ")
                                    mail = input("Ingrese el correo del empleado del empleado: ")
        case 2:
            print("Mostrar empleados")
        case 3:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción ingresada no es valida")
