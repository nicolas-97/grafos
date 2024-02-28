from recorrer import preorden_arbol_n_ario
from nodo import Nodo

def construir_arbol_n_ario(lista):
    if not lista:
        return None
    
    raiz = Nodo(lista[0])
    
    for sublista in lista[1:]:
        hijo = construir_arbol_n_ario(sublista)
        raiz.hijos.append(hijo)
    
    return raiz

arbol_lista = ['A', ['B', ['E'], ['F'], ['G']], ['C'], ['D', ['H']]]
arbol = construir_arbol_n_ario(arbol_lista)

print(preorden_arbol_n_ario(arbol))