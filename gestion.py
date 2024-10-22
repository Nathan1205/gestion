#Condicion del ciclo
seguir = True

#una funcion que crea un archivo
def n_file():
    try:
        #abre un archivo de texto pero sobrescribe cualquier info
        data = open("data.txt", "w")
    except:
        print('aiuda, llamen al inge')
    finally:
        data.close()
#funcion para escribir en un archivo con parentesis cuadrados
def w_file1(texto):
    try:
        data = open("data.txt", "a")
        data.write(f'[{texto}]')
    except:
        print('aiuda, llamen al inge')
    finally:
        data.close()
#funcion para escribir en un archivo sin parentesis cuadrados
def w_file2(texto):
    try:
        data = open("data.txt", "a")
        data.write(f"{texto}")
    except:
        print('aiuda, llamen al inge')
    finally:
        data.close()
#funcion para leer un archivo
def r_file():
    try:
        #abre el archivo y devuelve el texto en el.
        data = open('data.txt', 'r')
        return data.read()
    except FileNotFoundError:
        n_file()
    except SyntaxError:
        print('Porfavor ingrese datos al archivo antes de leerlo')
    finally:
        data.close()

'''
Sistema de administraccion de inventario y registro de ventas

Pasos para la creacion:
-Menu de bienvenida
    Incluir opciones tales como administrar inventario y un registo de compra y venta.
    La opcionn de cerrar el programa.

'''

#ciclo del menu

while seguir:
    print('''
Bienvenido al sistema administrativo, elija una opcion:
1-Administrar inventario.
2-Finanzas
3-Salir
4-Ver inventario

''')
    opcion = input('Ingrese el numero de la opcion que desea:')
    #Lleva al menu de inventario si la opcion es 1
    if opcion == '1':
        print('''
Elija una opcion:
1-Agregar adquisiciones.
2-Agregar cantidad.
''')
        choice = input("Ingrese el numero de la opcion deseada:")
        
        if choice == '1':
            #Opcion que lleva a poner el nombre del producto
            producto = input('Ingrese el nombre del producto:')
            productos = r_file()
            products_lst = eval(productos)
            w_file1(producto)
            print(products_lst)
        elif choice == '2':
            #opcion que lleva a cambiar la cantidad de cierto producto.
            nombre = input('Ingrese el nombre del producto cuya cantidad desea cambiar:')
            lista = r_file()
    #Lleva a finanzas para registrar ingresos o gastos monetarios
    elif opcion == '2':
        print(
                '''
                1-Aumentar ingresos
                2-Agregar gastos
                ''')
        n_file('monney')
        select = input('Ingrese el numero de la opcion deseada:')
    elif opcion == '3':
        print('El programa se cerro, adios!')
    
        seguir = False
    elif opcion == '4':
        print(r_file())


