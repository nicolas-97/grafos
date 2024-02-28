from nodo import Nodo

# Ejemplo de uso
# Creamos un árbol n-ario
"""
         A
       / | /
      B  C  D
     /|/    |
    E F G   H
"""



nodoA = Nodo('A')
nodoB = Nodo('B')
nodoC = Nodo('C')
nodoD = Nodo('D')
nodoE = Nodo('E')
nodoF = Nodo('F')
nodoG = Nodo('G')
nodoH = Nodo('H')

nodoA.hijos = [nodoB, nodoC, nodoD]
nodoB.hijos = [nodoE, nodoF, nodoG]
nodoD.hijos = [nodoH]


def preorden_arbol_n_ario(raiz: Nodo) -> list:
    if raiz is None:
        return
    path = [raiz.valor]
    for hijo in raiz.hijos:
        path.extend(preorden_arbol_n_ario(hijo))
    return path

print("Recorrido en preorden del árbol n-ario:")
print(preorden_arbol_n_ario(nodoA))

def postorden_arbol_n_ario(raiz: Nodo) -> list:
    if raiz is None:
        return
    path = []
    for hijo in raiz.hijos:
        path.extend(postorden_arbol_n_ario(hijo))
    path.append(raiz.valor)
    return path

print("Recorrido en postorden del árbol n-ario:")
print(postorden_arbol_n_ario(nodoA))

def inorden_arbol_n_ario(raiz):
    if raiz is None:
        return []
    path = []
    if len(raiz.hijos) > 0:
        path.extend(inorden_arbol_n_ario(raiz.hijos[0]))
        path.append(raiz.valor)
        
        for hijo in raiz.hijos[1:]:
            path.extend(inorden_arbol_n_ario(hijo))
    else:
        path.append(raiz.valor)
    
    return path

print("Recorrido en inorden del árbol n-ario:")
print(inorden_arbol_n_ario(nodoA))
