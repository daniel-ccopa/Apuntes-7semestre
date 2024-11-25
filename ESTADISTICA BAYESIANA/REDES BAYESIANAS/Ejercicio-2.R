# Cargar librerías
require(bnlearn)
require(qgraph)

# Crear la estructura vacía
red2 <- empty.graph(nodes = c("A", "B", "C", "D", "E", "F", "G"))

# Visualizar la red vacía
graf <- qgraph(red2, asize = 5, color = "lightgreen")

# Definir los arcos
arcos2 <- matrix(c("A", "C", 
                   "B", "C", 
                   "C", "D", 
                   "C", "E", 
                   "E", "F", 
                   "E", "G", 
                   "F", "G"), 
                 ncol = 2, byrow = TRUE, 
                 dimnames = list(NULL, c("from", "to")))

# Añadir arcos a la red
arcs(red2) <- arcos2

# Visualizar la red con las conexiones
qgraph(red2, asize = 5, color = "lightgreen", layout = graf$layout)

# Verificar los arcos añadidos
arcs(red2)

# Funciones adicionales para explorar la red
parents(red2, "C")  # Padres del nodo "C"

children(red2, "B")  # Hijos del nodo "B"

acyclic(red2)  # Verificar si la red es acíclica

