from collections import deque
from goodrich.ch14.graph import Graph


def vecinos(g, v):
    """Retorna una lista con los elementos de los vecinos de v."""
    resultado = []
    for e in g.incident_edges(v):
        vecino = e.opposite(v)
        resultado.append(vecino.element())
    return resultado


def dfs(g, v, d):
    """DFS desde v. Modifica d agregando vertices descubiertos."""
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)


def bfs(g, v):
    """BFS desde v usando una cola estandar."""
    d = {v: None}
    cola = deque([v])

    while cola:
        u = cola.popleft()
        for e in g.incident_edges(u):
            w = e.opposite(u)
            if w not in d:
                d[w] = e
                cola.append(w)
    return d


def alcanzables(g, v):
    """Retorna una lista con los elementos de los vertices alcanzables."""
    d = bfs(g, v)

    resultado = []
    for nodo in d.keys():
        resultado.append(nodo.element())
    return resultado


if __name__ == "__main__":
    pass
