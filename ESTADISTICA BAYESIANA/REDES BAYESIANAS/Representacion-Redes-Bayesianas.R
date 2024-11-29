# Cargar las librerías necesarias
require(bnlearn)  # Cargar bnlearn
require(qgraph)   # Cargar qgraph

# Crear la estructura de la Red Bayesiana (RB) con 5 nodos (A, B, C, D, E)
estr = empty.graph(LETTERS[1:5])

# Verificar la clase de la estructura creada
class(estr)
# Esto debería devolver: [1] "bn"

# Representación gráfica de la Red Bayesiana con aristas rojas
graf = qgraph(estr, asize=5, color="red")
graf
## From To Weight
##

arcos=matrix(c("A","C","B","E","C","E"), ncol = 2, byrow = TRUE, dimnames = list(NULL, c("from", "to")))
arcos
## from to
## [1,] "A" "C"
## [2,] "B" "E"
## [3,] "C" "E"
           
arcs(estr)=arcos
qgraph(estr, asize=5, color="red", layout=graf$layout)


# Adición de arcos a la RB
estr=set.arc(estr, from="D", to="A")
qgraph(estr, asize=5, color="red", layout=graf$layout)

estr=set.arc(estr, from="B", to="A")
qgraph(estr, asize=5, color="red", layout=graf$layout)


arcs(estr)


estr=reverse.arc(estr, from="D", to="A")
qgraph(estr, asize=5, color="red", layout=graf$layout)

arcs(estr)


# Funciónes de verificación de la estructura de la RB
parents(estr, "A")
## [1] "B"
narcs(estr)


children(estr, "B")
## [1] "A" "E"
ancestors(estr,"D")
## [1] "A" "B"
spouses(estr, "C")
## [1] "B"
acyclic(estr)

