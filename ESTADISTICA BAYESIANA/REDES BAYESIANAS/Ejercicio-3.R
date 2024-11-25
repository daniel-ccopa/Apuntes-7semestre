# Cargar librerías
require(bnlearn)
require(qgraph)

# Crear la estructura vacía
red3 <- empty.graph(nodes = c("A", "B", "C", "D"))
red3

graf = qgraph(red3, asize=5, color="orange")

# Definir los arcos según las dependencias
arcos3 <- matrix(c("A", "B",
                   "A", "C",
                   "B", "C",
                   "C", "D"),
                 ncol = 2, byrow = TRUE, 
                 dimnames = list(NULL, c("from", "to")))

# Añadir los arcos a la red
arcs(red3) <- arcos3

# Visualizar la red con las conexiones
qgraph(red3, asize = 5, color = "orange", layout = graf$layout)

# Verificar los arcos añadidos
arcs(red2)

# Funciones adicionales para explorar la red
parents(red2, "C")  # Padres del nodo "C"

children(red2, "B")  # Hijos del nodo "B"

acyclic(red2)  # Verificar si la red es acíclica
