import funciones_btc
import validaciones_biblioteca1


def menu():
    print('\033[35m' + "--Menu de opciones--" + '\033[0;m')
    print('\033[36m' + "1_Carga de datos")
    print("2_Mostrar datos")
    print("3_Cantidad de libros por genero y Genero mas popular")
    print("4_Busqueda de mayor precio por idioma")
    print("5_Busqueda por ISBN para aumento de precio")
    print("6_Consutar libros del genero mas popular")
    print("7_Consulta de precio por grupo")
    print("8_Salir" + '\033[0;m')
    return int(input("Que opcion desea elegir?: "))


def cargar_libreria_random(n):
    v = [None] * n
    for i in range(n):
        v[i] = funciones_btc.cargar_libros_random()
    return v


def cargar_libreria_manual(n):
    v = [None] * n
    for i in range(n):
        v[i] = funciones_btc.cargar_manual()
    return v


def ordenar_por_titulo(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].titulo > v[j].titulo:
                v[i], v[j] = v[j], v[i]


def ordenar_precio(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].precio < v[j].precio:
                v[i], v[j] = v[j], v[i]


def mostrar_libreria(v):
    for libro in v:
        print(funciones_btc.to_string(libro))


def buscar_may_precio_idioma(v, i):
    may_precio = None
    for search in v:
        if search.idioma == i or search.isbn == i:
            if may_precio is None:
                may_precio = search
            elif may_precio.precio < search.precio:
                may_precio = search
    return may_precio


def contador_precios_libro(p):
    precios = 0
    for i in range(len(p)):
        precios += p[i].precio
    return precios


def buscar_por_isbn(v, i, op):
    for search in v:
        if op == 5:
            if search.isbn == i:
                suba_precio = (search.precio * 10) / 100
                search.precio += suba_precio
                return search
        elif op == 7:
            if search.isbn == i:
                return search
    return None


def cantidad_genero(v):
    cantidad = [0] * 10
    for i in range(len(v)):
        genero = v[i].genero
        cantidad[genero] += 1
    return cantidad


def mayores(cantidad):
    mayor_genero = 0
    mayor = cantidad[0]
    for i in range(1, len(cantidad)):
        if cantidad[i] > mayor:
            mayor_genero = i
            mayor = cantidad[i]
    return mayor_genero, mayor


def principal():
    GENEROS = ["Autoayuda", "Arte", "Ficcion", "Computacion", "Economia", "Escolar", "Sociedad", "Gastronomia", "Infantil", "Otros"]
    v = []
    op = -1
    while op != 8:
        op = menu()
        if op == 1:
            carga = validaciones_biblioteca1.validar_entre(1, 2, '\033[33m' + "Elija (1) para carga manual o (2) para carga automatica: " + '\033[0;m')
            if carga == 1:
                validar = validaciones_biblioteca1.validar_desde("Ingrese la cantidad de libros a cargar: ", 0)
                v = cargar_libreria_manual(validar)
            else:
                validar = validaciones_biblioteca1.validar_desde("Ingrese la cantidad de libros a cargar: ", 0)
                v = cargar_libreria_random(validar)
        elif op == 2:
            if len(v) == 0:
                print("Ingrese los datos primero.")
            else:
                ordenar_por_titulo(v)
                mostrar_libreria(v)
        elif op == 3:
            total = cantidad_genero(v)
            print('\033[35m' + "Cantidad de libros por generos: " + '\033[0;m')
            for i in range(len(total)):
                print("Genero", GENEROS[i], "-", total[i], "Libro(s)")
            mayor, cantidad = mayores(total)
            print("\033[32mEl genero con mayor cantidad de libros ofrecidos es ", GENEROS[mayor], " con una cantidad de: ", cantidad, sep="")
        elif op == 4:
            idioma_int = input('\033[33m' + "Ingrese el idioma que desea buscar: " + '\033[0;m')
            x = buscar_may_precio_idioma(v, idioma_int)
            if x is None:
                print('\033[31m' + "No se encontraron libros de ese idioma." + '\033[0;m')
            else:
                print(funciones_btc.to_string(x))
        elif op == 5:
            isbn_search = input('\033[33m' + "Ingrese el ISBN que desea buscar: " + '\033[0;m')
            isbn_founded = buscar_por_isbn(v, isbn_search, op)
            if isbn_founded is None:
                print('\033[31m' + "No se encontraron libros con ese ISBN." + '\033[0;m')
            else:
                print(funciones_btc.to_string(isbn_founded))
        elif op == 6:
            print("\033[31mLos libros del genero mas popular:")
            total = cantidad_genero(v)
            mayor, cantidad = mayores(total)
            ordenar_precio(v)
            for i in range(len(v)):
                if mayor == v[i].genero:
                    print(funciones_btc.to_string(v[i]))
        elif op == 7:
            busqueda_valida = validaciones_biblioteca1.validar_desde("Cuantos libros desea buscar?: ", 0)
            total_pagar = 0
            for i in range(busqueda_valida):
                x = input("Busque un libro por ISBN: ")
                isbn = buscar_por_isbn(v, x, 7)
                if isbn is None:
                    print('\033[31m' + "Lo sentimos ese libro no se encuentra disponible en nuestro catalogo." + '\033[0;m')
                else:
                    total_pagar += isbn.precio
                    print('\033[32m' + "Se ha encontrado el libro que estaba buscando." + '\033[0;m')
                    print(funciones_btc.to_string(isbn))
            print('\033[32m' + "El total a pagar es de " + '\033[0;m$', total_pagar)


if __name__ == '__main__':
    principal()
