# Cargar librerías
require(bnlearn)
require(qgraph)

# Crear la estructura vacía
red4 <- empty.graph(nodes = c("Comida", "Tifoidea", "Reacciones", "Fiebre", "Gripe", "Dolor"))

# Visualizar la red vacía
graf <- qgraph(red4, asize = 5, color = "yellow")

# Definir los arcos según las dependencias
arcos4 <- matrix(c("Comida", "Tifoidea",
                   "Tifoidea", "Reacciones",
                   "Tifoidea", "Fiebre",
                   "Gripe", "Fiebre",
                   "Fiebre", "Dolor"),
                 ncol = 2, byrow = TRUE, 
                 dimnames = list(NULL, c("from", "to")))

# Añadir los arcos a la red
arcs(red4) <- arcos4

# Visualizar la red con las conexiones
qgraph(red4, asize = 5, color = "yellow", layout = graf$layout)

# Verificar los arcos añadidos
arcs(red4)

# Funciones adicionales para explorar la red
parents(red4, "Reacciones")  # Padres del nodo "Reacciones"

children(red4, "Tifoidea")  # Hijos del nodo "Tifoidea"

acyclic(red4)  # Verificar si la red es acíclica

