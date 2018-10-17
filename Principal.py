from MemoriaDinamica import *
lista = []
instrumentos = ['guitarra','violin', 'sax', 'piano', 'bajo']
precios = [100, 50, 200, 170, 800]

listas = MemoriaDinamica(instrumentos)
listas.imprimirLista()
listas.recorrerArreglo()
listas.imprimirLista()
listas.agregarelementoarray('notas')
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.eliminarElemento('guitarra')
listas.imprimirLista()
instrumentos.pop(4)
listas.imprimirLista()
listas.insertarNPosicion(2, 'marca')
listas.imprimirLista()
lista2 = MemoriaDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(100)
lista2.imprimirLista()
