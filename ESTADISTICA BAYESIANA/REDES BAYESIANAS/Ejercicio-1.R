# Cargar librerías
require(bnlearn)
require(qgraph)

# Crear la estructura vacía de la Red Bayesiana
red1 <- empty.graph(nodes = c("A", "B", "C", "D", "E"))

# Visualizar la red vacía
graf <- qgraph(red1, asize = 5, color = "lightblue")

# Definir los arcos según las relaciones del ejercicio
arcos1 <- matrix(c("A", "C",  # A -> C
                   "B", "C",  # B -> C
                   "C", "E",  # C -> E
                   "B", "D"), # B -> D
                 ncol = 2, byrow = TRUE, 
                 dimnames = list(NULL, c("from", "to")))

# Añadir los arcos a la red
arcs(red1) <- arcos1

# Visualizar la red con las conexiones
qgraph(red1, asize = 5, color = "lightblue", layout = graf$layout)

# Verificar los arcos añadidos
arcs(red1)

# Funciones adicionales para explorar la red
parents(red1, "C")  # Padres del nodo "C"

children(red1, "B")  # Hijos del nodo "B"

acyclic(red1)  # Verificar si la red es acíclica
