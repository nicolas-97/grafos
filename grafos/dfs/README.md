## Algoritmo de Búsqueda en Profundidad (DFS)

El algoritmo de Búsqueda en Profundidad (DFS) es un algoritmo utilizado para recorrer o buscar en un grafo de manera más profunda, explorando un camino hasta su fin antes de retroceder. La lógica detrás de este algoritmo es la siguiente:

1. **Inicio desde un nodo inicial**: El algoritmo DFS comienza explorando un nodo inicial (o nodo de inicio) dado.

2. **Exploración en profundidad**: A partir del nodo de inicio, DFS explora uno de sus nodos vecinos no visitados. Una vez que selecciona un vecino no visitado, continúa la exploración desde ese vecino, eligiendo otro nodo vecino no visitado, y así sucesivamente, profundizando en el grafo tanto como sea posible antes de retroceder.

3. **Marca de nodos visitados**: Durante la exploración, cada nodo visitado se marca para evitar volver a visitarlo. Esto ayuda a evitar ciclos infinitos en grafos con ciclos.

4. **Retroceso (backtracking)**: Cuando DFS alcanza un nodo que no tiene más vecinos no visitados, retrocede (backtracks) al nodo anterior para explorar otros caminos desde ese nodo. DFS continúa retrocediendo hasta que no haya más nodos por explorar o hasta que se hayan visitado todos los nodos accesibles desde el nodo inicial.

5. **Finalización**: El algoritmo DFS se considera completo una vez que se han visitado todos los nodos accesibles desde el nodo inicial.

En resumen, el algoritmo DFS se enfoca en explorar en profundidad antes de retroceder y explorar otros caminos. Es útil para la detección de ciclos, la exploración exhaustiva de grafos, la generación de árboles de expansión en árboles de búsqueda y la resolución de problemas de búsqueda en profundidad.
