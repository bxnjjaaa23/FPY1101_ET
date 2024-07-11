import csv
import os
import time
from random import*
acceso=1
trabajadores=[
    ['Juan Perez'],
      ['Maria Garcia'], 
      ['Carlos Lopez'], 
      ['Ana Martinez'], 
      ['Pedro Rodriguez'], 
      ['Laura Hernandez'], 
      ['Miguel Sanchez'], 
      ['Isabel Gomez'], 
      ['Francisco Diaz'], 
      ['Elena Fernandez']]
def menu():
    limpiar()
    print(''' Menu
          1) Asignar sueldo aleatorio
          2) Clasificar sueldos
          3) Ver estadisticas
          4) Reporte de sueldos
          5) Salir del programa''')
    while acceso==1:
        try:
            opc=int(input('Porfavor elija una opcion del 1-4: '))
        except ValueError:
            print('Porfavor elija una opcion valida')
            continue
        if opc==1:
            limpiar()
            asigsueldo()
            volver()
        elif opc==2:
            limpiar()
            calificarsueldo()
            imprimir()
            volver()
        elif opc==3:
            limpiar()
            volver()
        elif opc==4:
            limpiar()
            volver()
        elif opc==5:
            limpiar()
            salir()
        else:
            print('Porfavor elija una opcion valida')

datos=f'''{trabajadores}'''
with open('trabajadores.txt', 'w', newline='')as arichivo_txt:
    arichivo_txt.write(datos)


def imprimir():
    with open('trabajadores.txt', 'r')as arichivo_txt:
        for lista in arichivo_txt:
            print(lista)

sueldo=[]


def asigsueldo():
        for sueldo in trabajadores:
            sueldo=randint(300000, 2500000)
 
            
        print('Sueldos asignados correctamente ')


def calificarsueldo():
    print(sueldo)
    if sueldo<800000:
        print('hola')
    elif sueldo >= 800000 and sueldo<2000000:
        print('soy')
    elif sueldo >2000000:
        print('yo')


        
#def estadisticas():
        
def crear():
    with open('Reporte de sueldos.csv', 'w', newline='') as reporte_csv:
        reporte_csv=csv.writer(reporte_csv)
        reporte_csv.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])

def guardar(sueldo,reporte_csv):
    with open('Reporte de sueldos.csv', 'a', newline='') as reporte_csv:
        reporte_csv=csv.writer(reporte_csv)
        reporte_csv.writerow([sueldo])
        
def volver():
    while acceso==1:
        try:
            opc=int(input('''Desea volver al menu? 
                        Presione 1 para Si
                        Presione 2 para No
                        Respuesta:  '''))
        except ValueError:
            print('Porfavor elija una opcion valida ')
            continue
        if opc==1:
            print('Volviendo...')
            time.sleep(0.3)
            menu()
        elif opc==2:
            salir()
        else:
            print('Porfavor elija una opcion valida')
        
def limpiar():
    os.system('cls')
        
def salir():
    print('Finalizando programa...')
    time.sleep(0.3)
    print('Desarrollado por Benjamin Arriaza')
    print('Rut 22.051.788-8')
    time.sleep(0.3)
    quit()
        
menu()