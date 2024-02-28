## Algoritmo de Búsqueda en Amplitud (BFS)

El algoritmo de Búsqueda en Amplitud (BFS) es un algoritmo utilizado para recorrer o buscar en un grafo de manera más ancha, es decir, explora todos los nodos vecinos de un nodo antes de pasar a los nodos vecinos de los vecinos. La lógica detrás de este algoritmo es bastante simple:

1. **Inicio**: Comienza desde un nodo de inicio dado.

2. **Cola de nodos por visitar**: Utiliza una cola para mantener un seguimiento de los nodos que se deben visitar. Inicialmente, el nodo de inicio se agrega a la cola.

3. **Marcar como visitado**: Marca el nodo de inicio como visitado.

4. **Recorrer nodos vecinos**: Mientras la cola no esté vacía, saca un nodo de la cola (generalmente el primero que entró) y lo considera como el nodo actual. Luego, examina todos los nodos vecinos del nodo actual.

5. **Visitar nodos vecinos no visitados**: Para cada nodo vecino del nodo actual, si el vecino no ha sido visitado, lo marca como visitado y lo agrega a la cola. Esto asegura que los nodos vecinos se visiten en un orden "en amplitud", es decir, todos los nodos a una distancia de 1 del nodo actual se visitan antes de pasar a los nodos a una distancia de 2, y así sucesivamente.

6. **Repetir el proceso**: Repite los pasos 4 y 5 hasta que la cola esté vacía, lo que indica que se han visitado todos los nodos accesibles desde el nodo de inicio.

En resumen, el algoritmo BFS se basa en la idea de explorar primero todos los nodos vecinos antes de pasar a los nodos a una mayor profundidad en el grafo. Esto garantiza que los nodos se visiten en un orden "en amplitud" y es útil para encontrar caminos más cortos en un grafo no ponderado y para la búsqueda en general cuando se desea visitar todos los nodos accesibles desde un nodo de inicio dado.
