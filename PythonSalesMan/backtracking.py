import graph_lib as gl
import math
import sys
import queue
import dijkstra
import copy


def next(current_v: gl.Vertex, current_e: gl.Edge, visits: list, g: gl.Graph, final: gl.Vertex):

    global path, best_path

    previs = current_e.Destination.Prev

    if (
        current_v not in previs
        and len(previs) < 2
        and path[0] + current_e.Length < best_path[0]
        and (current_e.Destination in visits or len(current_e.Destination.Edges) > 1)
    ):

        previs.append(current_v)
        path[0] += current_e.Length
        path[1].append(current_e)

        fet = False
        try:
            visits.remove(current_e.Destination)
            fet = True
        except ValueError:
            pass

        backtrack_rec(g, visits, current_e.Destination, final)

        if fet:
            visits.append(current_e.Destination)
        path[0] -= current_e.Length
        path[1].pop()
        previs.pop()


def backtrack_rec(g: gl.Graph, visits: list, current_v: gl.Vertex, final: gl.Vertex):

    global path, best_path

    if current_v == final and not visits and path[0] < best_path[0]:
        best_path[0] = path[0]
        best_path[1] = path[1].copy()
    else:
        [
            next(current_v, current_e, visits, g, final)
            for current_e in sorted(current_v.Edges, key=lambda x: x.Length)
        ]

# ============================= BACKTRACKING PUR =============================

def SalesmanTrackBacktracking(g: gl.Graph, visits: list):

    global path, best_path
    best_path = [math.inf, []]
    path = [0, []]

    for vertex in g.Vertices:
        vertex.Prev = []

    restants = visits.Vertices[1:]
    primer = visits.Vertices[0]
    ultim = visits.Vertices[-1]

    backtrack_rec(g, restants, primer, ultim)

    result = gl.Track(g)
    result.Edges = best_path[1]
    return result


# ============================ BACKTRACKING GREEDY ============================


def SalesmanTrackBacktrackingGreedy(g: gl.Graph, visits: gl.Visits):
    raise NotImplementedError("Funció no implementada")