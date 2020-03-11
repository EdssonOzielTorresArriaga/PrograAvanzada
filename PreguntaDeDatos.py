#Importa el modulo requerido para usar datos de tipo Date.
import datetime
#Los datos se tienen, se preguntan o se calculan y pueden ser de diferente tipo.
# str (string), i (int), f (float), dt (date).
def main():
    #Los datos se tienen, se preguntan o se calculan y pueden ser de diferente tipo.
    # str (string), i (int), f (float), dt (date).
    strDato = input("Dame un dato string: ")
    #Los numericos SP por intermediacion.
    _iDato = input("Dame un dato entero: ")
    iDato = int(_iDato)
    _fDato = input("Dame un dato float: ")
    fDato = float(_fDato)
    #Los datos se preguntan por intermediacion.
    _dtDato = input("Dame una fecha yyyy/mm/dd: ")
    # [n,m] Extrae de la posición n a la posición m,sin incluir m.
    # [-m:] Extrae desde la posición m, de atrás para adelante, hasta el final.
    
    año=_dtDato[0:4]
    mes=_dtDato[5:7]
    dia=_dtDato[-2:]
    print(año)
    print(mes)
    print(dia)
    
    dtDato = datetime.datetime(int(año), int(mes), int(dia))
    
    print(strDato)
    print(type(strDato))
    print(iDato)
    print(type(iDato))
    print(fDato)
    print(type(fDato))
    print(dtDato)
    print(type(dtDato))
    