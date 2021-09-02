import random
import validaciones_biblioteca1

GENEROS = "Autoayuda", "Arte", "Ficcion", "Computacion", "Economia", "Escolar", "Sociedad", "Gastronomia", "Infantil", "Otros"
IDIOMAS = "Español", "Ingles", "Frances", "Italiano", "Otros"
TITULOS = "Pocahonda", "Aprende Python sin practica", "La bella y la bestia", "AED for noob", "Algebra IV", "Mejorar en Counter Strike"


class Libro:
    def __init__(self, isbn, titulo, genero, idioma, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


def to_string_genero(gen):
    str_genero = ()
    for i in range(len(GENEROS)):
        if gen == i:
            str_genero = GENEROS[i]
    return str_genero


def to_string(libro):
    texto = "ISBN: {} - Titulo: {} - Genero: {} - Idioma: {} - Precio: ${}"
    return texto.format(libro.isbn, libro.titulo, to_string_genero(libro.genero), libro.idioma, libro.precio)


def cargar_libros_random():
    isbn_n = validaciones_biblioteca1.generar_isbn()
    isbn = validaciones_biblioteca1.to_string_isbn(isbn_n)
    titulo = random.choice(TITULOS)
    genero = random.randint(0, 9)
    idioma = random.choice(IDIOMAS)
    precio = random.randrange(300, 10000, 500)
    libro = Libro(isbn, titulo, genero, idioma, precio)
    return libro


def cargar_manual():
    isbn = input("Ingrese el ISBN: ")
    valid = validaciones_biblioteca1.validar_isbn(isbn)
    while not valid:
        isbn = input("Ingrese un ISBN VALIDO!: ")
        valid = validaciones_biblioteca1.validar_isbn(isbn)
    titulo = input("Ingrese el titulo del libro: ")
    print("(0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros)")
    genero = validaciones_biblioteca1.validar_entre(0, 9, "Ingresa el codigo del genero de su libro: ")
    print("IDIOMAS: Español, Ingles, Frances, Italiano, Otros")
    idioma = validaciones_biblioteca1.validar_idioma("Ingrese el idioma del libro: ")
    precio = validaciones_biblioteca1.validar_desde("Ingrese el precio del libro: ", 0)
    libro = Libro(isbn, titulo, genero, idioma, precio)
    return libro


if __name__ == '__main__':
    x = cargar_libros_random()
    print(to_string(x))
