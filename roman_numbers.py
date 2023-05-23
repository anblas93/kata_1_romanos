unidades = {1: "I", 5: "V", 10: "X"}
decenas = {1: "X", 5: "L", 10: "C"}
centenas = {1: "C", 5: "D", 10: "M"}
millares = {1: "M"}

class RomanNumberError(Exception):
    pass

def listar_numero(num):
    n_mil = num // 1000 * 1000
    n_cen = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10) 
    return [n_mil, n_cen, n_dec, n_uni]

def sacar_clave(num):
    if num >= 1000:
        clave = millares
        num = num // 1000
    elif num >= 100:
        clave = centenas
        num = num // 100
    elif num >= 10:
        clave = decenas
        num = num // 10
    else:
        clave = unidades
    return clave, num

def logica_aplastante(digito, clau):
    res = ""
    if digito < 4:
        res = res + digito * clau[1]
    elif digito == 4:
        res = res + clau[1] + clau[5]
    elif digito < 9:
        num_palitos = digito - 5
        res += clau[5] + num_palitos * clau[1]
    else:
        res += clau[1] + clau[10]
    return res

def entero_a_romano(n_int):
    if n_int > 3999:
        raise RomanNumberError("RomanNumber must be less than 4000")
    
    digitos = listar_numero(n_int)

    resultado = ""
    for digito in digitos:
        if digito == 0:
            continue

        clave, digito = sacar_clave(digito)

        resultado += logica_aplastante(digito, clave)

    return resultado

if __name__ == "__main__":
    print(entero_a_romano(11))