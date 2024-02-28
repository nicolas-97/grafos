## Algoritmo de Dijkstra

El algoritmo de Dijkstra es un algoritmo de búsqueda de caminos más cortos diseñado para encontrar el camino más corto desde un nodo de origen hacia todos los demás nodos en un grafo dirigido ponderado, donde los pesos de las aristas son no negativos. A continuación, se presenta una descripción detallada del algoritmo:

### Descripción del algoritmo:

1. **Inicialización**: Se comienza asignando una distancia inicial de 0 al nodo de inicio y una distancia infinita a todos los demás nodos. También se crea un conjunto de nodos no visitados que inicialmente contiene todos los nodos del grafo.

2. **Selección del nodo**: En cada iteración, se selecciona el nodo con la distancia mínima entre los nodos no visitados.

3. **Actualización de distancias**: Se actualizan las distancias de los nodos vecinos del nodo seleccionado si se encuentra un camino más corto a través del nodo seleccionado.

4. **Marcar el nodo como visitado**: Una vez que se han actualizado todas las distancias vecinas, el nodo seleccionado se marca como visitado y se elimina del conjunto de nodos no visitados.

5. **Repetición del proceso**: Se repiten los pasos 2, 3 y 4 hasta que todos los nodos hayan sido visitados o hasta que no queden nodos accesibles desde el nodo de inicio.

### Características principales del algoritmo:

- **Eficiente**: El algoritmo de Dijkstra es eficiente y tiene una complejidad de tiempo de O(V^2) para implementaciones simples utilizando matrices de adyacencia, donde V es el número de nodos en el grafo. Con implementaciones más avanzadas, la complejidad puede reducirse a O((V + E) * log V), donde E es el número de aristas en el grafo.

- **Requiere pesos no negativos**: Dijkstra requiere que los pesos de las aristas sean no negativos. Aristas con pesos negativos pueden llevar a resultados incorrectos o a ciclos infinitos.

- **Encuentra el camino más corto**: Dijkstra encuentra el camino más corto desde el nodo de inicio hacia todos los demás nodos en un grafo dirigido ponderado con pesos no negativos.

- **Aplicaciones**: El algoritmo de Dijkstra se utiliza en sistemas de navegación, enrutamiento de redes, planificación de rutas de transporte, optimización de redes, y en otros campos donde se requiere encontrar rutas o caminos más cortos.

En resumen, el algoritmo de Dijkstra es una herramienta poderosa para encontrar el camino más corto desde un nodo de inicio hacia todos los demás nodos en un grafo ponderado con pesos no negativos. Su eficiencia y precisión lo hacen ampliamente utilizado en una variedad de aplicaciones prácticas.
