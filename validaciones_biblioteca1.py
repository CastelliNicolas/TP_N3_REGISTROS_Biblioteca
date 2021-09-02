import random
numeros = "1234567890"

# VALIDACIONES GENERALES


def validar_desde(mensaje, desde):
    valor = int(input(mensaje))
    while valor <= desde:
        print('\033[31m' + "Valor invalido. Ingrese nuevamente." + '\033[0;m')
        valor = int(input(mensaje))
    return valor


def validar_entre(desde, hasta, mensaje):
    valor = int(input(mensaje))
    while valor < desde or valor > hasta:
        print('\033[31m' + 'Valor invalido. Ingrese nuevamente.' + '\033[0;m')
        valor = int(input(mensaje))
    return valor


def validar_idioma(mensaje):
    idioma = input(mensaje)
    if idioma != "Español" or idioma != "Ingles" or idioma != "Frances" or idioma != "Italiano" or idioma != "Otros":
        print('\033[31m' + "Idioma no disponible. Ingrese nuevamente." + '\033[0;m')
        idioma = input(mensaje)
    return idioma


# Generar ISBN

class isbn:
    def __init__(self, pais, editor, articulo, control):
        self.pais = pais
        self.editor = editor
        self.articulo = articulo
        self.control = control


def to_string_isbn(isbn):
    texto = "{}-{}-{}-{}"
    return texto.format(isbn.pais, isbn.editor, isbn.articulo, isbn.control)


def generar():
    pais = int(input("pais: "))
    editor = int(input("edior: "))
    articulo = int(input("articulo: "))
    control = int(input("control: "))
    codigos = isbn(pais, editor, articulo, control)
    return codigos


def generar_isbn():
    pais = random.randrange(11, 99, 11)
    editor = random.randrange(11, 999, 11)
    articulo = random.randrange(11, 999, 11)
    control = random.randrange(11, 99, 11)
    codigos = isbn(pais, editor, articulo, control)
    return codigos


def sumar_codigos(x):
    suma = 0
    pais = x.pais
    editor = x.editor
    articulo = x.articulo
    control = x.control
    suma += pais + editor + articulo + control
    return suma


def validar_isbn(x):
    acum = 0
    factor = 10
    cont_guion = 0
    anterior = None
    for num in x:
        if num != "-":
            valor = int(num)
            calculo = (valor * factor)
            factor -= 1
            acum += calculo
            anterior = num
        elif anterior != num:
            cont_guion += 1
    if (acum % 11) == 0 and cont_guion == 3:
        print("ISBN Valido")
        return True
    else:
        print("ISBN no Valido")
        return False


if __name__ == '__main__':
    x = generar()
    print(to_string_isbn(x))
    print(sumar_codigos(x))
    print(validar_isbn(to_string_isbn(x)))

