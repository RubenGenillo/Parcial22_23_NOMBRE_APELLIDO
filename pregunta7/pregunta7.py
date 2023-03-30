class Nodo(object):

    info, sig = None, None


class datoPolinomio(object):
    def __init__(self,valor,termino):
        self.valor = valor
        self.termino = termino



class Polinomio(object):
    def __init__(self):
        self.temino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.temino_mayor
            polinomio.temino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.temino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux    
    
    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.temino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux = polinomio.temino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        

    def mostrar(polinomio):
        aux = polinomio.temino_mayor
        pol = ''
        if (aux is not None):
            while (aux is not None):
                signo = ' '
                if (aux.info.valor == 0):
                    signo += ' + '
                pol += signo + str(aux.info.valor) + 'x^' + str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def sumar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = polinomio1.obtener_valor( i) + polinomio2.obtener_valor( i)
            if (total != 0):
                paux.agregar_termino( i, total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.temino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.temino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if (paux.obtener_valor(termino) != 0):
                    valor += paux.obtener_valor( termino)
                    paux.modificar_termino( termino, valor)
                else:
                    paux.agregar_termino( termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def eliminar(polinomio, termino):
        aux = polinomio.temino_mayor
        siguiente = aux.sig
        while(siguiente is not None and siguiente.info.termino > termino):
            aux = aux.sig
            siguiente = aux.sig
        if (siguiente is not None and siguiente.info.termino == termino):
            aux.sig = siguiente.sig

    def existe_termino(polinomio, termino):
        aux = polinomio.temino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return True
        else:
            return False
        
    def restar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = polinomio1.obtener_valor( i) - polinomio2.obtener_valor( i)
            if (total != 0):
                paux.agregar_termino( i, total)
        return paux
    
    def dividir(polinomio1, polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.temino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.temino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if (paux.obtener_valor(termino) != 0):
                    valor += paux.obtener_valor( termino)
                    paux.modificar_termino( termino, valor)
                else:
                    paux.agregar_termino( termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    
    def dividir2(polinomio1, polinomio2):
            pauxNue = Polinomio()
            
            
            pauxRes = Polinomio()
            if (polinomio1.grado > polinomio2.grado):
                mayor = polinomio1 
                menor = polinomio2
            else:
                mayor = polinomio2  
                mayor = polinomio1

            pauxMenor = menor

            while (mayor.info.termino >= menor.termino):
                terminoMayorPuntual = mayor.temino_mayor
                aux = Polinomio()
                while(pauxMenor is not None):
                    nuevotermino = pauxMenor.info.termino + (terminoMayorPuntual - pauxMenor.info.termino)
                    aux.agregar_termino(nuevotermino, pauxMenor.info.valor*(mayor.info.valor/menor.info.valor))
                    pauxMenor = pauxMenor.sig
                pauxNue.agregar_termino(mayor.restar(aux).info.termino,mayor.restar(aux).info.valor)
                mayor.agregar_termino(mayor.restar(aux).info.termino,mayor.restar(aux).info.valor)
            return pauxNue

        
if __name__ == "__main__":

    prueba1 = Polinomio()
    prueba1.agregar_termino(0, 1)
    prueba1.agregar_termino(1, 2)
    prueba1.agregar_termino(2, 3)
    print(prueba1.mostrar())
    prueba2 = Polinomio()
    prueba2.agregar_termino(0, 1)
    prueba2.agregar_termino(1, 2)
    prueba2.agregar_termino(2, 1)
    print(prueba2.mostrar())
    print(prueba1.restar( prueba2).mostrar())
    